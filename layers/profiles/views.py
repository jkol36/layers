from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def home(request):
	if request.POST:
		userform = UserForm(request.POST)
		if userform.is_valid():
			print "view is printing"
		else:
			print userform.errors
	forms  = {'userform':UserForm}
	return render(request, 'testing.jade', {'forms':forms})
