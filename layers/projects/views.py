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
		form = NewProject(request.POST, profile=profile_id)
		if form.is_valid():
			instance = form.save()
			project_id = instance.id
			request.session['project_id'] = project_id
			messages.success(request, 'Awesome! Now lets add some pics.')
			forms = {'newprojectform':NewProject}
			return render(request, 'inspiration.jade', {'forms':forms, 'add_project':True, 'project':project_id})
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			forms = {'newprojectform':NewProject}
			return render(request, 'idea.jade', {'forms':forms})
	
	if request.session['project_id']:
		project_id = request.session['project_id']
		return render(request, 'inspiration.jade', {'forms':forms, 'project':project_id})
	else:
		return render(request, 'idea.jade', {'forms':forms, 'add_project':True})

@login_required
def add_photo_to_project(request):
	project_id = request.session['project_id']
	if request.FILES:
		added_photos = request.session['added_photos'] = True 
		form = add_photo_form(request.POST, request.FILES, project_id=project_id)
		if form.is_valid():
			print 'valid'
			form.save()
		else:
			print form.errors
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			return render(request, 'inspiration.jade')
	elif request.POST and request.session['added_photos'] == True:
		return redirect('my_account')
	return render(request, 'inspiration.jade', {'project':project_id})


