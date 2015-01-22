from django.shortcuts import render, redirect
from .forms import signup_for_emails_form
from django.contrib import messages


# Create your views here.

def signup_for_emails(request):
	if request.POST:
		print request.POST
		form = signup_for_emails_form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'You have signed up for emails!')
			return redirect('home')
		else:
			for t, z in form.errors:
				messages.error(request, t + z.as_text())
			return redirect('home')
	return render(request, 'index.jade')
