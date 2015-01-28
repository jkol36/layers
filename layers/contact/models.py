from django.db import models

# Create your models here.

class Feedback(models.Model):
	email = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	text = models.CharField(max_length=250)

	def __unicode__(self):
		return self.text


