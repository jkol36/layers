from django import forms
from layers.profiles.models import Profile, Layers_Profile
from .models import Project, Photo
from django.contrib import messages
from sorl.thumbnail import ImageField
from datetime import date
import time
from datetime import datetime


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
			if e.args[0] == 'profile':
				pass
			else:
				raise forms.ValidationError('Something went wrong.')

		return super(NewProject, self).__init__(*args, **kwargs)
	
	
	def clean_due_date(self):
		due_date = self.cleaned_data['due_date']
		year = int(due_date[0:4])
		month = int(due_date[5:7])
		day = int(due_date[8:])
		due_date_object = date(year, month, day)
		print due_date_object
		today = date.fromtimestamp(time.time())
		print today
		ship_date = abs(due_date_object - today).days
		if ship_date < 14:
			raise forms.ValidationError('Your order will take at least 2 weeks to design and develop. Please select a later date.')
		else:
			return due_date
	def clean_budget(self):
		budget = self.cleaned_data['budget']
		if '$' in budget:
			cleaned_budget = budget.split('$')[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		else:
			cleaned_budget = budget
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		


	def save(self):
		print self.profile_id
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

class add_photo_form(forms.ModelForm):
	class Meta:
		model = Photo
		exclude = ['caption', 'project']


	def __init__(self, *args, **kwargs):
		try:
			self.project_id = kwargs.pop('project_id')
		except Exception, e:
			pass
		super(add_photo_form, self).__init__(*args, **kwargs)
	
	def is_valid(self):
		valid = super(add_photo_form, self).is_valid()
		if valid == False:
			return valid
		try:
			project_id = int(self.data['project'])
		except Exception, DoesNotExist:
			pass
		self.cleaned_data['project'] = int(self.data['project'])
		try:
			for f in self.files.getlist('file'):
				self.cleaned_data['image'] = f
		except Exception, NoPhotos:
			raise forms.ValidationError('You did not add any photos')
		return True

	def save(self):
		try:
			project_id = self.cleaned_data['project']
			print type(project_id)
			photo = self.cleaned_data['image']
			print photo
			project = Project.objects.get(pk=project_id)
			print project
			f = Photo.objects.create(image=photo, project=project)
			f.save()
		except Exception, e:
			raise forms.ValidationError(e)




		



		
		
		


		

