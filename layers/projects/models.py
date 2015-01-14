from django.db import models
from layers.profiles.models import *
from sorl.thumbnail import ImageField

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=250, blank=False)
	description = models.CharField(max_length=400, blank=False)
	client = models.ForeignKey(Layers_Profile, default=False, blank=True, null=True, related_name="client")
	designer = models.ForeignKey(Layers_Profile, default=False, blank=True, null=True, related_name="designer")
	budget = models.IntegerField(null=True, blank=True)
	due_date = models.DateField(null=False, blank=False)
	designer_assigned = models.BooleanField(default=False, blank=True)


	def __unicode__(self):
		return self.title

	def get_project_description(self):
		return self.description

	def get_project_budget(self):
		return self.budget

	def get_project_due_date(self):
		return self.due_date

	def has_designer_been_assigned(self):
		return self.designer_assigned

class Photo(models.Model):
	caption = models.CharField(max_length=250, blank=True, null=True)
	image = ImageField(upload_to='/project_pics/')
	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.caption



