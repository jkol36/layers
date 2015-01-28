from django import forms
from .models import Subscriber



class signup_for_emails_form(forms.ModelForm):
	email = forms.CharField(widget=forms.EmailInput())

	class Meta:
		model = Subscriber
		fields = ['email']





	
