import mailchimp

def get_mailchimp_api():
	return mailchimp.Mailchimp("cb878902ccc52aae323de65d2045ea03-us3")

def add_subscriber(email=None, first_name=None, last_name=None, list_id="43eaa152c3"):
	api = get_mailchimp_api()
	try:
		api.lists.list.subscribe(list_id, {'email':'%s', 'FNAME':'%s', 'LNAME':'%s'} %(email, first_name, last_name))
	except Exception, e:
		return e