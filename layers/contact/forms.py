from django import forms
from .models import Feedback

class contactus(forms.ModelForm):
	email = forms.EmailField()
	name = forms.CharField()
	text = forms.CharField()

	class Meta:
		model = Feedback
		fields = ['name', 'email', 'text']





