from django.shortcuts import render
from django.contrib import messages
from layers.profiles.models import Profile, Layers_Profile
from layers.profiles.forms import PartialProfileForm
from layers.projects.forms import NewProject


# Create your views here.

def get_started(request):
	session_key = request.session.session_key
	try:
		profile = request.session['profile']
	except Exception, NoProfile:
		profile = ''

	try:
		project = request.session['project']
	except Exception, NoProject:
		project = ''

	print profile == ''
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
			messages.success(request, 'Project successfully created!')
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
		forms = [PartialProfileForm, NewProject]
		for form in forms:
			f = form(request.POST)
			if f.is_valid():
				instance = f.save()
				if instance.email:
					request.session['profile'] = instance.id
				elif instance.title:
					request.session['project'] = instance.id
			else:
				errors = f.errors.items()
				for i, z in errors:
					messages.error(request, i + z.as_text())

				#if the errors don't have to do with profile
				#we'll know because request.session['profile'] won't be an ''
				if request.session['profile'] != '':
					profile_id = request.session['profile']
					profile = Profile.objects.get(pk=profile_id)
					#we just have to render idea.jade with the project form
					forms = {'newprojectform':NewProject}
					return render(request, 'idea.jade', {'forms':forms, 'profile':profile})	
				return render(request, 'idea.jade', {'userform':PartialProfileForm, 'newprojectform':NewProject})



	if profile != '':
		forms = {'newprojectform':NewProject}
		profile_id = request.session['profile']
		profile = Profile.objects.get(pk=profile_id)
		return render(request, 'idea.jade', {'forms':forms, 'profile':profile})
	forms = {'userform':PartialProfileForm, 'newprojectform':NewProject}
	return render(request, 'idea.jade', {'forms':forms})

def add_photo(request, project, email):
	return render(request, 'inspiration.jade')