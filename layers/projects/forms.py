from django import forms
from layers.profiles.models import Profile, Layers_Profile
from .models import Project

class NewProject(forms.ModelForm):
	title = forms.CharField(label='Give your project a one sentence Title *', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"eg. Madison's Bridesmaids necklaces"}))
	description = forms.CharField(label="Give your project a description *", widget=forms.Textarea(attrs={"class":'form-control', 'placeholder':"This brief will be used by your designer to bring your idea to life. So the more specific the better."}))
	budget = forms.CharField(label="Budget", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'eg. Min $100'}))
	due_date = forms.CharField(label="Due Date", widget=forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}))

	class Meta:
		model = Project
		fields = ['title', 'description', 'budget', 'due_date']

