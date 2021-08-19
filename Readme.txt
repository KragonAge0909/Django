- Dependencies
	Python==3.8
	Django==2.2.3
	django-crispy-forms==1.1
	mysqlclient
	pytz==2019.1
	widget_tweaks
	crispy-form
- Installation
	1. Create a mysql database with its name - emaildb
	2. Django CLI
		python manage.py makemigrations
		python manage.py migrate
		python manage.py runserver
	3. setting.py
		EMAIL_HOST_USER = 'yourgmail@gmail.com'
		EMAIL_HOST_PASSWORD = 'yourgmailpassword'
- errors
	project/core/tokens.py
		# from django.utils import six
		import six

- Descriptions
	Custom User & Admin of Default Django
	Sending an Email through smtp gmail & webmaster.
	