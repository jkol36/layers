from django import forms
from .models import Profile, Layers_Profile
from django.core.validators import validate_email

#used for new users to create a Profile. (For authentication purposes)
class UserForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control', 'placeholder':'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

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
		layers_profile = Layers_Profile.objects.create(profile=profile)
		profile.save()
		return profile


#This form creates a new profile instance with Just a Firstname, LastName, and Email.
#This form can then be associated with a 43 Layers Profile so the user can start projects before signing up.

class PartialProfileForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your Email'}))

	class Meta:
		model = Profile
		fields = ['name', 'email']


	def clean_name(self):
		name = self.cleaned_data['name']
		try:
			last_name = name.split()[1]
		except Exception, NoLastName:
			raise forms.ValidationError('Please enter a last name')		
		return name


	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			p = Profile.objects.get(email=email)
		except Exception, ProfileDoesNotExist:
			print ProfileDoesNotExist
			return email

		raise forms.ValidationError('Email already taken')


	def save(self):
		name = self.cleaned_data['name'].split()
		first_name = name[0]
		last_name = name[1]
		email = self.cleaned_data['email']
		profile = Profile.objects.create(email=email, username=email, first_name=first_name, last_name=last_name)
		profile.save()
		layers_profile = Layers_Profile.objects.create(profile=profile)
		layers_profile.save()
		return profile

#This form adds authentication capability to a Profile Instance that doesn't yet have a Password associated with it.
class PasswordForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = Profile
		fields = ['password1', 'password2']

	def is_valid(self):
		valid = super(PasswordForm, self).is_valid()
		if valid == False:
			return valid
		else:
			if self.cleaned_data['password1'] and self.cleaned_data['password2']:
				password1 = self.cleaned_data['password1']
				password2 = self.cleaned_data['password2']
				if password1 != password2:
					raise forms.ValidationError("password's don't match")
				return True
			else:
				raise forms.ValidationError("You did not fill out both password forms.")

	def save(self):
		password = self.cleaned_data['password1']
		profile_id = self.data['profile']
		profile = Profile.objects.get(pk=profile_id)
		profile.set_password(password)
		profile.save()
		return password

class UpdateSettings(forms.ModelForm):
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your Email'}))
	notification_emails = forms.BooleanField(required=False)
	news_letter = forms.BooleanField(required=False)

	class Meta:
		model = Layers_Profile
		fields = ['email', 'notification_emails', 'news_letter']

	
	def __init__(self, *args, **kwargs):
		try:
			self.profile = kwargs.pop('profile')
		except Exception, e:
			pass

		return super(UpdateSettings, self).__init__(*args, **kwargs)
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			profiles = Profile.objects.get(username=email)
			print profiles
		except Exception, EmailDoesNotExist:
			print EmailDoesNotExist
			return email
		raise forms.ValidationError('Somehow that email is already taken...')

	def save(self):
		profile_id = self.profile
		profile = Profile.objects.get(pk=profile_id)
		email = self.cleaned_data['email']
		email_notifications = self.cleaned_data['notification_emails']
		news_letter = self.cleaned_data['news_letter']
		profile.username = email
		profile.email = email
		profile.save()
		layers_profile = Layers_Profile.objects.get(profile=profile)
		layers_profile.notification_emails = email_notifications
		layers_profile.newsletter = news_letter
		layers_profile.save()
		return profile



















	
