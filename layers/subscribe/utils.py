import mailchimp

def get_mailchimp_api():
	return mailchimp.Mailchimp("cb878902ccc52aae323de65d2045ea03-us3")

def add_subscriber(email=None, first_name=None, last_name=None, list_id="43eaa152c3"):
	api = get_mailchimp_api()
	print email
	print first_name
	print last_name

	#try:
	#	api.lists.subscribe(list_id, {'email':email, 'FNAME':first_name, 'LNAME':last_name}
	#except Exception, e:
		#return e