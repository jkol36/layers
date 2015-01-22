from django.db import models

# Create your models here.

class Subscriber(models.Model):
	email = models.CharField(max_length=250)

	def __unicode__(self):
		return self.email
