from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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


