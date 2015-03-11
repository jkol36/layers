from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from layers.profiles.forms import UserForm
from layers.contact.forms import contactus
from layers.subscribe.utils import add_subscriber
import logger
logger = logging.getLogger(__name__)

# Create your views here.

def login_view(request):
	if not request.POST:
		return render(request, 'login.jade')
	
	username = request.POST['email']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('my_account')
		
	messages.error(request, 'Oops. It looks like you submitted the wrong username or password.')
	return render(request, 'login.jade')


def signup_view(request):
	if not request.POST:
		return render(request, 'signup.jade', {'forms':UserForm})
	
	form = UserForm(request.POST)
	print request.POST
	if not form.is_valid():
		for t,z in form.errors.items():
			messages.error(request, t + z.as_text())
			logger.error(t+z.as_text())
		return render(request, 'signup.jade', {'forms':UserForm})
		
	form.save()
	
	messages.success(request, 'Your account was successfully created! Now Login.')
	return redirect('login')
		

def blog(request):
	if not request.POST:
		return render(request, 'blog.jade')

def faq(request):
	if not request.POST:
		return render(request, 'faq.jade')

def about(request):
	return render(request, 'about.jade')

def terms(request):
	return render(request, 'terms.jade')

def privacy(request):
	return render(request, 'privacy.jade')

def contact(request):
	if not request.POST:
		return render(request, 'contact.jade')

	
	form = contactus(request.POST)
	if not form.is_valid():
		for t,z in form.errors.items():
			messages.error(request, t + z.as_text())
			logger.error(t+z.as_text())
		return render(request, 'contact.jade')
		
	form.save()
	messages.success(request, "Your message has been sent! Thanks for contacting us.")
	return render(request, 'contact.jade')





