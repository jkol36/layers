from django import forms
from .models import Profile, Layers_Profile

#used for new users to create a 43 Layers Profile.
class UserForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


	def is_valid(self):
		print "is valid form printing"


	
