from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from layers.profiles.forms import UserForm
from layers.contact.forms import contactus

# Create your views here.

def login_view(request):
	if request.POST:
		username = request.POST['email']
		print username
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('my_account')
		else:
			messages.error(request, 'Oops. It looks like you submitted the wrong username or password.')
	return render(request, 'login.jade')


def signup_view(request):
	if request.POST:
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your account was successfully created! Now Login.')
			return redirect('login')
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			return render(request, 'signup.jade', {'forms':UserForm})
	return render(request, 'signup.jade', {'forms':UserForm})

def blog(request):
	if request.POST:
		pass
	else:
		return render(request, 'blog.jade')

def faq(request):
	if request.POST:
		pass
	else:
		return render(request, 'faq.jade')

def about(request):
	return render(request, 'about.jade')

def terms(request):
	return render(request, 'terms.jade')

def privacy(request):
	return render(request, 'privacy.jade')

def contact(request):
	if request.POST:
		form = contactus(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your message has been sent! Thanks for contacting us.")
		else:
			for t, z in form.errors.items():
				messages.error(request, t + z.as_text())
			return render(request, 'contact.jade')
	return render(request, 'contact.jade')





