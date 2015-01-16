from django.conf import settings
from layers.profiles.models import Layers_Profile

class Worker():
	def __init__(self, *args, **kwargs):
		try:
			self.profiles = kwargs.pop('profiles')
			if self.profiles:
				for profile in self.profiles:
					email = profile.email:
					self.send_mail(email)
		except Exception, NoProfiles:
			self.sleep_action()
	return super(Worker, self).__init__(*args, **kwargs)
	self.daemon = True


	def send_mail(email):
		import smptplib
		from smptplib.email import Message
		host = email_host
		username = email_username
		password = email_password

