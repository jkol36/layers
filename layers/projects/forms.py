from django import forms
from layers.profiles.models import Profile, Layers_Profile
from .models import Project
from django.contrib import messages


class NewProject(forms.ModelForm):
	title = forms.CharField(label='Give your project a one sentence Title *', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"eg. Madison's Bridesmaids necklaces"}))
	description = forms.CharField(label="Give your project a description *", widget=forms.Textarea(attrs={"class":'form-control', 'placeholder':"This brief will be used by your designer to bring your idea to life. So the more specific the better."}))
	budget = forms.CharField(label="", widget=forms.HiddenInput())
	due_date = forms.CharField(label="Due Date", widget=forms.DateInput(attrs={'class':'form-control', 'id':'duedate'}))

	class Meta:
		model = Project
		fields = ['title', 'description', 'budget', 'due_date']


	def __init__(self, *args, **kwargs):
		try:
			self.profile_id = kwargs.pop('profile')
		except Exception, e:
			pass
		return super(NewProject, self).__init__(*args, **kwargs)
	
	def save(self):
		profile = Profile.objects.get(pk=self.profile_id)
		layers_profile = Layers_Profile.objects.get(pk=profile.accounts.id)
		layers_profile.has_projects = True
		title = self.cleaned_data['title']
		description = self.cleaned_data['description']
		budget = self.cleaned_data['budget']
		due_date = self.cleaned_data['due_date']
		new_project = Project.objects.create(title=title, description=description, budget=budget, due_date=due_date, client=layers_profile)
		new_project.save()
		layers_profile.save()
		return new_project
		
		
		


		

