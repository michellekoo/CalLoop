from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.
class Day(Model):
	days_of_week = (
		('Mon', 'Monday'), 
		('Tues', 'Tuesday'), 
		('Wed','Wednesday'),
		('Thurs','Thursday'), 
		('Fri','Friday'), 
		('Sat','Saturday'), 
		('Sun','Sunday'),
	)
	name = CharField(max_length=256, choices=days_of_week)

class Subject(Model):
	name = CharField(max_length=256)
	user = ManyToManyField(User)
	#weekday = ForeignKey(Day)

#comment
class Assignment(Model):
	name = CharField(max_length=256)
	user = ManyToManyField(User)
	due_date = DateTimeField()
	due_in = DurationField()
	subject = ForeignKey(Subject)


