from django.db import models
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField

# Create your models here.

class Profile(AbstractUser):
	pass

	def __unicode__(self):
		if self.username:
			return self.username
		else:
			return self.email


class Layers_Profile(models.Model):
	is_designer = models.BooleanField(default=False)
	has_projects = models.BooleanField(default=False)
	notification_emails = models.BooleanField(default=True)
	newsletter = models.BooleanField(default=True)
	profile = models.OneToOneField(Profile, related_name='accounts', null = True)
	Profile_Pic = ImageField(upload_to='/profile_pics/')
	has_profile_pic = models.BooleanField(default=False)
	session_key = models.CharField(max_length=250, null=True, blank=True)


	def __unicode__(self):
		return self.profile.email

	def get_designer_status(self):
		return self.is_designer

	def get_projects(self):
		return self.has_projects

	def get_picture_status(self):
		return self.has_profile_pic




