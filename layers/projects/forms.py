from django import forms
from layers.profiles.models import Profile, Layers_Profile
from .models import Project

class NewProject(forms.ModelForm):
	title = forms.CharField(label='Give your project a one sentence Title *', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"eg. Madison's Bridesmaids necklaces"}))
	description = forms.CharField(label="Give your project a description *", widget=forms.Textarea(attrs={"class":'form-control', 'placeholder':"This brief will be used by your designer to bring your idea to life. So the more specific the better."}))
	budget = forms.CharField(label="", widget=forms.HiddenInput())
	profiles = forms.ModelMultipleChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput(), label="")
	due_date = forms.CharField(label="Due Date", widget=forms.DateInput(attrs={'class':'form-control', 'id':'duedate'}))

	class Meta:
		model = Project
		fields = ['title', 'description', 'budget', 'profiles', 'due_date']

	def __init__(self, *args, **kwargs):
		super(NewProject, self).__init__(*args, **kwargs)
		if self.is_bound != False:
			print 'ok'
		else:
			pass
	def clean_budget(self):
		budget = self.cleaned_data['budget']
		if budget == '':
			raise forms.ValidationError('You did not specify a budget for your project')
		elif budget < 100:
			raise forms.ValidationError('Your budget is to small. You need to at least be willing to pay more than $100')
		else:
			return budget

	def clean_profiles(self, *args, **kwargs):
		print kwargs



	def save(self):
		print self.cleaned_data


		
		


		

