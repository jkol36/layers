from django import forms
from .models import Subscriber
from .utils import add_subscriber


class signup_for_emails_form(forms.ModelForm):
	email = forms.CharField(widget=forms.EmailInput())

	class Meta:
		model = Subscriber
		fields = ['email']


	def save(self):
		s = super(signup_for_emails_form, self).save()
		email = self.cleaned_data['email']
		add_email = add_subscriber(email=email)
		print add_email




	
