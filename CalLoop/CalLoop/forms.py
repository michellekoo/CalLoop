from django.forms import *

class Login(Form):
	username = CharField(label='Username', max_length=100)
	password = CharField(label='Password', max_length=15)

class NewUser(Form):
	first_name = CharField(label='First name', max_length=20)
	last_name = CharField(label='Last name', max_length=30)
	email = CharField(label='Email', max_length=40)
	username = CharField(label='Username', max_length=100)
	password = CharField(label='Password', max_length=15)
	reenter = CharField(label='Password', max_length=15)
