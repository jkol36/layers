from django import forms
from .models import Profile, Layers_Profile
from django.core.validators import validate_email

#used for new users to create a 43 Layers Profile.
class UserForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = Profile
		fields = ['name', 'email', 'password1', 'password2']


	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			Profile.objects.get(email=email)
		except Exception, ProfileDoesNotExist:
			return email
		raise forms.ValidationError('Email is already Taken')


	def clean_password(self):
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		else:
			return password1

	def clean_name(self):
		name = self.cleaned_data['name'].split()
		try:
			first_name = name[0]
			print first_name
		except Exception, NoFirstName:
			raise forms.ValidationError('Please Enter your Name')
		try:
			last_name = name[1]
			print last_name
		except Exception, NoLastName:
			raise forms.ValidationError('Please enter a last name')
		return name
	
	def save(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		password = self.cleaned_data['password1']
		first_name = name[0]
		last_name = name[1]
		profile = Profile.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
		profile.set_password(password)
		profile.save()
		return profile








	
