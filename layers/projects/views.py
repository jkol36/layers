from django.shortcuts import render, redirect
from layers.profiles.models import Profile, Layers_Profile
from .models import Project, Photo
from django.contrib.auth.decorators import login_required
from .forms import add_photo_form, NewProject
from django.contrib import messages

# Create your views here.

@login_required
def add_project(request):
	profile_id = request.user.id
	forms = {'newprojectform':NewProject}
	if request.POST:
		print "should submit is {}".format(request.POST.get('should_submit', ''))
		should_submit = request.POST.get('should_submit', '')
		if should_submit != '':
			request.session['should_submit'] = should_submit
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
def add_photo_to_project(request):

	try:
		project_id = request.session['project_id']
	except Exception, NoProjectID:
		project_id = False
	project = Project.objects.get(pk=project_id)
	photos = Photo.objects.filter(project=project)
	if request.FILES:
		added_photos = request.session['added_photos'] = True 
		form = add_photo_form(request.POST, request.FILES, project_id=project_id)
		if form.is_valid():
			#if the form is valid clear the session
			#now when the user adds another project, he'll start from the add_project view.
			form.save()
			return render(request, 'project_status.jade', {'project':project, 'photos': photos})
		else:
			print form.errors
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			return render(request, 'inspiration.jade')
	elif request.POST and not request.FILES:
		print "the value of should_submit is {}".format(request.POST.get('should_submit', ''))
		if not request.POST.get('should_submit', '') == "true":
			p = Project.objects.get(pk=project_id)
			p.project_status = "submit_idea"
			p.save()
			print p.project_status
		request.session.__delitem__('project_id')


		return render(request, 'project_status.jade', {'project':project, 'photos': photos})
	elif request.POST and request.session['added_photos'] == True:
		return render(request, 'project_status.jade', {'project': project, 'photos':photos})
	
	return render(request, 'inspiration.jade', {'project':project_id})

@login_required
def project_status(request):
	try:
		project_id = request.GET['project_id']
	except Exception, NoID:
		messages.error('No Project Id')
		return redirect('my_account')
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
	

