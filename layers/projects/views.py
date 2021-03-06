from django.shortcuts import render, redirect
from layers.profiles.models import Profile, Layers_Profile
from .models import Project, Photo, Project_Applicant
from django.contrib.auth.decorators import login_required
from .forms import add_photo_form, NewProject, editProject
from django.contrib import messages
from django.db.models import Q
import logging
logger = logging.getLogger(__name__)

# Create your views here.

@login_required
#adds a project to the users profile 
def add_project(request):
	profile_id = request.user.id
	forms = {'newprojectform':NewProject}

	if request.POST:
		print "should submit is {}".format(request.POST.get('should_submit', ''))
		form = NewProject(request.POST, profile=profile_id)
		if form.is_valid():
			print "valid"
			instance = form.save()
			project_id = instance.id
			request.session['project_id'] = project_id
			messages.success(request, "Awesome! Now let's add some pics.")
			forms = {'newprojectform':NewProject}
			return redirect('add_photo', project_id)
		else:
			print "not valid"
			for t, z in form.errors.items():
				print t, z
				messages.error(request, t + z.as_text())
				logger.error(t + z.as_text())

			forms = {'newprojectform':NewProject}
			return render(request, 'idea.jade', {'forms':forms, 'add_project':True})
	
	try:
		project_id =  request.session['project_id']
		return render(request, 'inspiration.jade', {'forms':forms, 'project_id':project_id, 'add_project':True})
	except Exception, NoId:
		forms = {'newprojectform':NewProject}
		return render(request, 'idea.jade', {'forms':forms, 'add_project':True})

@login_required
# adds a photo to a project
def add_photo_to_project(request, project_id=None):
	if project_id == None:
		project_id = request.session.get('project_id', '')
	else:
		project_id = project_id
	
	if request.method == "GET" and not request.is_ajax():
		return render(request, 'inspiration.jade', {'project_id':project_id, 'add_project':True})
	elif request.method =="GET" and request.is_ajax():
		pass
	if request.method =="POST" and request.FILES:
		form = add_photo_form(request.POST, request.FILES, project_id=project_id)
		if form.is_valid():
			#if the form is valid clear the session
			#now when the user adds another project, he'll start from the add_project view.
			form.save()
			if not request.POST.get('should_submit', '') == "true":
				p = Project.objects.get(pk=project_id)
				p.project_status = "submit_idea"
				p.save()
				return redirect('project_status', project_id)
			else:
				return redirect('my_account')

		else:
			for t, z in form.errors.items():
				messages.error(request, t+z.as_text())
				logger.error(t+z.as_text())
			return redirect('add_photo_to_project', project_id)

	elif request.method == "POST" and not request.FILES:
		if not request.POST.get("should_submit", '') == "true":
			p = Project.objects.get(pk=project_id)
			p.project_status = "submit_idea"
			p.save()
			return redirect('project_status', project_id)

		try:
			request.session.__delitem__('project_id')
		except KeyError:
			pass
		return redirect('project_status', project_id)
	


@login_required
def project_status(request, project_id):
	
	try:
		project = Project.objects.get(pk=project_id)
	except Exception, NoProject:
		messages.error('That Project does not exist')
		return redirect('my_account')
	try:
		photos = project.photo_set.all()
	except Exception, e:
		photos = None

	try:
		request.GET["is_designer"]
	except Exception:
		return render(request, 'project_status.jade', {'project':project, 'photos':photos})
	return render(request, 'project_status.jade', {'project':project, 'photos':photos, 'is_designer':True})
@login_required
def all_projects(request):
	all_projects = Project.objects.filter(Q(designer_assigned=False, project_status="submit_idea") | Q(project_status="assigning_designer")).exclude(Q(client=request.user.accounts) | Q(designer=request.user.accounts))
	my_projects = Project.objects.filter(designer=request.user.accounts)
	projects_applied_to = Project_Applicant.objects.filter(designer=request.user.accounts)
	print dir(request.user.accounts)
	return render(request, 'designer_view.jade', {'projects':all_projects, 'my_projects':my_projects, 'pending_projects':projects_applied_to})



@login_required
def edit_project(request, project_id):
	if not request.POST:
		return redirect('my_account')

	elif request.POST and request.FILES:
		form = add_photo_form(request.POST, request.FILES, project_id = project_id)
		if form.is_valid():
			form.save()
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
				logger.error(t+z.as_text())
			return redirect('project_status', project_id)
	elif request.POST and not request.FILES:
		form = editProject(request.POST, project_id=project_id)
		if form.is_valid():
			print "valid"
			form.save()
			messages.success(request, 'Project Updated!')
			return redirect('project_status', project_id)
		else:
			print form.errors
			logger.error(form.errors)

		return redirect('project_status', project_id)


def start_project(request, project_id):
	if not request.POST:
		return redirect('my_account')

	else:
		project = Project.objects.get(pk=project_id)
		project.project_status = "assigning_designer"
		project.save()
		return redirect('my_account')
	

def bid_project(request, project_id, designer_id):
	if request.POST:
		project = Project.objects.get(pk=project_id)
		designer = Layers_Profile.objects.get(pk=designer_id)
		project_applicant = Project_Applicant.objects.get_or_create(project=project, designer=designer)
		messages.success(request, "We've recieved your request to work on this project. You should here from us shortly!")
		return redirect('all_projects')
	else:
		return redirect('all_projects')
	




