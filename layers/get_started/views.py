from django.shortcuts import render
from layers.profiles.models import Profile, Layers_Profile
from layers.profiles.forms import PartialProfileForm
from layers.projects.forms import NewProject

# Create your views here.

def get_started(request):
	forms = {'userform':PartialProfileForm, 'newprojectform':NewProject}
	return render(request, 'idea.jade', {'forms':forms})
