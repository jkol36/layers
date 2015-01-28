from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from layers.profiles.models import Profile, Layers_Profile
from layers.profiles.forms import PartialProfileForm
from layers.projects.forms import NewProject, add_photo_form


# Create your views here.

def get_started(request):
	profile = request.session.get('profile', default='')
	project = request.session.get('project', default='')
	project_has_images = request.session.get('project_has_images', 'default=False')
	
	#if the user is posting but has a profile.
	if request.POST and profile != '':
		#We pass the submitted form along with the profile instance
		form = NewProject(request.POST, profile=profile)
		#if the form is valid
		if form.is_valid():
			#save the form
			#returns the newly created instance
			instance = form.save()
			#set the project instance to the id of the returned form
			request.session['project'] = instance.id
			#Send a message to the user letting him know that his project was created
			messages.success(request, 'Project successfully created! Now lets add some photos.')
			return render(request, 'inspiration.jade', {'profile':profile, 'project':request.session['project'] })
		#if the form isn't valid, return the error messages raised by the form validation.
		else:
			for i, z in form.errors.items():
				messages.error(request, i + z.as_text())
			#create a new instance of the project form
			forms = {'newprojectform':NewProject}
			#render the template again, this time with the profile fields filled out.
			return render(request, 'idea.jade', {'forms':forms})
	#If the user doesn't have a profile
	elif request.POST and profile == '':
		#user is submitting info to the Partial Profile Form and the Project Form
		form = PartialProfileForm(request.POST)
		if form.is_valid():
			instance = form.save()
			request.session['profile'] = instance.id
			profile = request.session['profile']
			new_project = NewProject(request.POST, profile=profile)
			if new_project.is_valid():
				i = new_project.save()
				project_id = i.id
				messages.success(request, 'Awesome! Now Lets add some pictures.')
				return render(request, 'inspiration.jade', {'profile':profile, 'project':project_id})
			#if our project form is not valid
			else:
				for t,z in new_project.errors.items():
					messages.error(request, t + z.as_text())
				forms = {'newprojectform':NewProject}
				return render(request, 'idea.jade', {'forms':forms, 'profile':profile})
		#if our user form is not valid
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			forms = {'newprojectform':NewProject, 'userform':PartialProfileForm}
			return render(request, 'idea.jade', {'forms':forms} )


		
		#must pass the profile id and project id to the template
		return render(request, 'inspiration.jade', {'profile':profile_id, 'project':project_id})

	
	if profile != '' and project != '' and project_has_images != False:
		return redirect('home')
	elif profile != '' and project != '':
		return render(request, 'inspiration.jade', {'profile':profile, 'project':project})
	elif profile != '':
		forms = {'newprojectform':NewProject}
		profile_id = request.session['profile']
		profile = Profile.objects.get(pk=profile_id)
		return render(request, 'idea.jade', {'forms':forms, 'profile':profile})

	forms = {'userform':PartialProfileForm, 'newprojectform':NewProject}
	return render(request, 'idea.jade', {'forms':forms})

def submit_design(request):
	profile = request.session.get)'profile', default="")
	
	if not request.FILES:
		return redirect(reverse('complete_signup'))
	
	form = add_photo_form(request.POST, request.FILES)
	if not form.is_valid():
		for t, z in form.errors:
			messages.error(request, t + z.as_text())
	form.save()
	return HttpResponse('success')
	
		











