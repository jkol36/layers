from django.db import models
from layers.profiles.models import *
from sorl.thumbnail import ImageField

# Create your models here.

class Project(models.Model):
	STATUS_CHOICES = (
		('submit_idea', 'Submit Idea'),
		('Design Center', 'Design Center'),
		('Shipping', 'Shipping'),
		('Complete', 'Completed Order'),
		)
	title = models.CharField(max_length=250, blank=False)
	description = models.CharField(max_length=400, blank=False)
	client = models.OneToOneField(Layers_Profile, default=False, blank=True, null=True, related_name="client")
	designer = models.OneToOneField(Layers_Profile, default=False, blank=True, null=True, related_name="designer")
	budget_min = models.IntegerField(null=True, blank=True)
	budget_max = models.IntegerField(null=True, blank=True)
	due_date = models.DateField(null=False, blank=False)
	designer_assigned = models.BooleanField(default=False, blank=True)
	project_status = models.CharField(choices=STATUS_CHOICES, max_length=250, default='submit_idea', null=True, blank=True)
	is_completed = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
	
	def get_is_completed(self):
		return self.is_completed
	def get_project_status(self):
		return self.project_status
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
	image = ImageField(upload_to='project_pics/', blank=True, null=True)
	project = models.ForeignKey(Project)

	



