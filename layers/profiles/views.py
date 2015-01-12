from django.shortcuts import render
from .models import Profile
from .forms import UserForm, PartialProfileForm, PasswordForm

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


def complete_signup(request, profile, project):
	return render(request, 'complete_signup.jade')


def my_account(request):
	pass


