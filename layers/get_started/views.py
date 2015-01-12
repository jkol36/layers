from django.shortcuts import render
from django.contrib import messages
from layers.profiles.models import Profile, Layers_Profile
from layers.profiles.forms import PartialProfileForm
from layers.projects.forms import NewProject


# Create your views here.

def get_started(request):
	if request.POST:
		email = []
		userform = PartialProfileForm(request.POST)
		if userform.is_valid():
			email.append(userform.instance)
			userform.save()
		else:
			for i, z in userform.errors.items():
				messages.error(request,i + z.as_text())
		new_product = NewProject(request.POST, email)
		if new_product.is_valid():
			new_product.save()
		else:
			for i, z in new_product.errors.items():
				messages.error(request, i + z.as_text())


	forms = {'userform':PartialProfileForm, 'newprojectform':NewProject}
	return render(request, 'idea.jade', {'forms':forms})
