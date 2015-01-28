from django.shortcuts import render, redirect
from .forms import signup_for_emails_form
from django.contrib import messages


# Create your views here.

def signup_for_emails(request):
	if not request.POST:
		return render(request, 'index.jade')

	
	form = signup_for_emails_form(request.POST)
	if not form.is_valid():
		messages.error(request, t + z.as_text() for t, z in form.errors)

	form.save()
	messages.success(request, 'You have signed up for emails!')
	return redirect('home')
