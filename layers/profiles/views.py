from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from layers.projects.models import Project
from django.contrib import messages
from .forms import UserForm, PartialProfileForm, PasswordForm, UpdateSettings
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
	if request.POST:
		userform = PartialProfileForm(request.POST)
		if userform.is_valid():
			email = userform.instance
			userform.save()
		else:
			print userform.errors
	forms  = {'userform':PartialProfileForm}
	return render(request, 'index.jade', {'forms':forms})


def complete_signup(request):
	profile_id = request.session['profile']
	profile = Profile.objects.get(pk=profile_id)
	email = profile.email
	first_name = profile.first_name
	if request.POST:
		form = PasswordForm(request.POST)
		if form.is_valid():
			password = form.save()
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, 'You are now logged in!')
				return redirect('my_account')


		else:
			print form.errors
	return render(request, 'signup.jade', {'email':email, 'first_name':first_name, 'profile':profile_id})

@login_required
def my_account(request):
	try:
		has_profile_pic = request.user.accounts.has_profile_pic
	except Exception, NoAccounts:
		has_profile_pic = False
		print NoAccounts
	try:
		projects = Project.objects.filter(client=request.user.accounts)
	except Exception, NoProjects:
		projects = False
	print request.user
	if projects:
		request.user.accounts.has_projects = True
	else:
		pass
	forms = {'UpdateSettings':UpdateSettings}
	return render(request, 'account.jade', {'profile_pic':has_profile_pic, 'forms':forms, 'projects':projects})

def logout_view(request):
	logout(request)
	return redirect('home')

def update_settings(request):
	if request.POST:
		form = UpdateSettings(request.POST, profile=request.user.id)
		if form.is_valid():
			form.save()
			messages.success(request, 'Info Updated')
			return redirect('my_account')
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			return redirect('my_account')
	return redirect('my_account')


		








