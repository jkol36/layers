from django import forms
from layers.profiles.models import Profile, Layers_Profile
from .models import Project, Photo
from django.contrib import messages
from sorl.thumbnail import ImageField
from datetime import date
import time
from datetime import datetime


class NewProject(forms.ModelForm):
	title = forms.CharField(label='* Give Your Project A One Sentence Title', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"eg. Madison's Bridesmaids Necklaces"}))
	description = forms.CharField(label="* Give Your Project A Description", widget=forms.Textarea(attrs={"class":'form-control', 'placeholder':"This brief will be used by your designer to bring your idea to life, so the more specific the better."}))
	budget_min = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'class':'display-none'}))
	budget_max = forms.CharField(required=False,widget=forms.HiddenInput(attrs={'class':'display-none'}))
	due_date = forms.CharField(required=False, label="Due Date", widget=forms.DateInput(attrs={'class':'form-control', 'id':'duedate'}))

	class Meta:
		model = Project
		fields = ['title', 'description', 'budget_min', 'budget_max', 'due_date']
		exclude = ['budget_min', 'budget_max']


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
		if not due_date:
			return None
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
	def clean_budget_max(self):
		budget_max = self.cleaned_data['budget_max']
		if not budget_max:
			return None
		if ',' in budget_max and '$' in budget_max:
			budget_split = budget_max.split(',')
			cleaned_budget_max = budget_split[0] + budget_split[1]
			cleaned_budget = cleaned_budget_max.split('$')[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				return forms.ValidationError("You should have a budget of at least $100")

		elif not ',' in budget_max and '$' in budget_max:
			cleaned_budget = budget_max.split('$')[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		elif not '$' in budget_max and ',' in budget_max:
			budget_max_split = budget_max.split(',')
			cleaned_budget = budget_max_split[0] + budget_max_split[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100')
		else:
			cleaned_budget = budget_max
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		
	def clean_budget_min(self):
		budget_min = self.cleaned_data['budget_min']
		if not budget_min:
			return None
		# if a comma and a cash sign are submitted
		if ',' in budget_min and '$' in budget_min:
			budget_min_split = budget_min.split(',')
			budget_min_cleaned = budget_min_split[0] + budget_min_split[1]
			print "budget min cleaned {}".format(budget_min_cleaned)
			cleaned_budget_min = budget_min_cleaned.split('$')[1]
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				return forms.ValidationError("You should have a budget of at least $100")
		# if there's no comma but there is a cash sign 
		elif not ',' in budget_min and '$' in budget_min:
			cleaned_budget_min = budget_min.split('$')[1]
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		
		elif not '$' in budget_min and ',' in budget_min:
			cleaned_budget_min = budget_min.split(',')
			budget_min_cleaned = cleaned_budget_min[0] + cleaned_budget_min[1]
			if int(cleaned_budget_min) >= 100:
				return budget_min_cleaned
			else:
				raise forms.ValidationError('You should have a budget of at least $100')
		else:
			cleaned_budget_min = budget_min
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')


	def save(self):
		print self.profile_id
		profile = Profile.objects.get(pk=self.profile_id)
		layers_profile = Layers_Profile.objects.get(pk=profile.accounts.id)
		layers_profile.has_projects = True
		title = self.cleaned_data['title']
		description = self.cleaned_data['description']
		budget_max = self.cleaned_data['budget_max']
		budget_min = self.cleaned_data['budget_min']
		due_date = self.cleaned_data['due_date']
		new_project = Project.objects.create(title=title, description=description, project_status='assigning_designer', budget_min=budget_min, budget_max=budget_max, due_date=due_date, client=layers_profile)			
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
			print DoesNotExist
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


class editProject(forms.ModelForm):
	title = forms.CharField(required=False)
	description = forms.CharField(required=False)
	budget_min = forms.CharField(required=False)
	budget_max= forms.CharField(required=False)
	due_date = forms.CharField(required=False)

	class Meta:
		model = Project
		fields = ['title', 'description', 'budget_min', 'budget_max', 'due_date']

	def __init__(self, *args, **kwargs):
		self.project_id = kwargs.pop('project_id')
		self.project = Project.objects.get(pk=self.project_id)
		
		super(editProject, self).__init__(*args, **kwargs)
		
		
	
	def clean_title(self):
		if not "newProjectTitle" in self.data:
			return None
		new_title = self.data.get('newProjectTitle')
		return new_title

	def clean_description(self):
		if not "newProjectDescription" in self.data:
			return None

		new_description = self.data.get("newProjectDescription")
		return new_description

	def clean_budget_min(self):
		if not "newBudgetMin" in self.data:
			return None
		budget_min = self.data.get('newBudgetMin')
		if ',' in budget_min and '$' in budget_min:
			budget_min_split = budget_min.split(',')
			budget_min_cleaned = budget_min_split[0] + budget_min_split[1]
			print "budget min cleaned {}".format(budget_min_cleaned)
			cleaned_budget_min = budget_min_cleaned.split('$')[1]
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				return forms.ValidationError("You should have a budget of at least $100")
		# if there's no comma but there is a cash sign 
		elif not ',' in budget_min and '$' in budget_min:
			cleaned_budget_min = budget_min.split('$')[1]
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		
		elif not '$' in budget_min and ',' in budget_min:
			cleaned_budget_min = budget_min.split(',')
			budget_min_cleaned = cleaned_budget_min[0] + cleaned_budget_min[1]
			if int(cleaned_budget_min) >= 100:
				return budget_min_cleaned
			else:
				raise forms.ValidationError('You should have a budget of at least $100')
		else:
			cleaned_budget_min = budget_min
			if int(cleaned_budget_min) >= 100:
				return cleaned_budget_min
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')


	def clean_budget_max(self):
		if not "newBudgetMax" in self.data:
			return None

		budget_max = self.data.get("newBudgetMax")
		if ',' in budget_max and '$' in budget_max:
			budget_split = budget_max.split(',')
			cleaned_budget_max = budget_split[0] + budget_split[1]
			cleaned_budget = cleaned_budget_max.split('$')[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				return forms.ValidationError("You should have a budget of at least $100")

		elif not ',' in budget_max and '$' in budget_max:
			cleaned_budget = budget_max.split('$')[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')
		elif not '$' in budget_max and ',' in budget_max:
			budget_max_split = budget_max.split(',')
			cleaned_budget = budget_max_split[0] + budget_max_split[1]
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100')
		else:
			cleaned_budget = budget_max
			if int(cleaned_budget) >= 100:
				return cleaned_budget
			else:
				raise forms.ValidationError('You should have a budget of at least $100.')

	def save(self):
		if self.cleaned_data.get('title'):
			self.project.title = self.cleaned_data['title']
		
		elif self.cleaned_data.get('budget_min'):
			self.project.budget_min = self.cleaned_data['budget_min']

		elif self.cleaned_data.get('budget_max'):
			self.project.budget_max = self.cleaned_data['budget_max']

		elif self.cleaned_data.get('due_date'):
			self.project.due_date = self.cleaned_data['due_date']

		elif self.cleaned_data.get('description'):
			self.project.description = self.cleaned_data['description']
		self.project.save()




		




	


	
	
		


		



		
		
		


		

