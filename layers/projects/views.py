from django.shortcuts import render, redirect
from layers.profiles.models import Profile, Layers_Profile
from .models import Project, Photo
from django.contrib.auth.decorators import login_required
from .forms import add_photo_form, NewProject, editProject
from django.contrib import messages
from django.db.models import Q

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
			return render(request, 'inspiration.jade', {'forms':forms, 'add_project':True, 'project':project_id})
		else:
			print "not valid"
			for t, z in form.errors.items():
				print t, z
				messages.error(request, t + z.as_text())

			forms = {'newprojectform':NewProject}
			return render(request, 'idea.jade', {'forms':forms, 'add_project':True})
	
	try:
		project_id =  request.session['project_id']
		return render(request, 'inspiration.jade', {'forms':forms, 'project':project_id, 'add_project':True})
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
	try:
		if request.GET:
			return render(request, 'inspiration.jade', {'project_id':project_id})

		if request.POST== "POST" and request.FILES:
			form = add_photo_form(request.POST, request.FILES, project_id=project_id)
			if form.is_valid():
				#if the form is valid clear the session
				#now when the user adds another project, he'll start from the add_project view.
				form.save()
				if not request.POST.get('should_submit', '') == "true":
					p = Project.objects.get(pk=project_id)
					p.project_status = "submit_idea"
					p.save()
					photos = Photo.objects.filter(project=p)
				return redirect('project_status', project_id)

			else:
				for t, z in form.errors.items():
					messages.error(request, t+z.as_text())
				return redirect('add_photo_to_project', project_id)

		elif request.POST and not request.FILES:
			print dir(request.sesssion)
			return redirect('project_status', project_id)
	except ValueError:
		pass


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
		
	return render(request, 'project_status.jade', {'project':project, 'photos':photos})

@login_required
def all_projects(request):
	projects = Project.objects.filter(Q(designer_assigned=False, project_status="submit_idea") | Q(project_status="assigning_designer"))
	return render(request, 'designer_view.jade', {'projects':projects})



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
			return redirect('project_status', project_id)

	form = editProject(request.POST)
	if form.is_valid():
		form.save()
		messages.success(request, 'Project Updated!')
		return redirect('project_status')
	else:
		print form.errors

	return redirect('project_status')

	





