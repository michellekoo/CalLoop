from django.db.models import *

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
	weekday = ManyToManyField(Day)


class Assignment(Model):
	name = CharField(max_length=256)
	due_date = DateTimeField()
	due_in = DurationField()
	subject = ForeignKey(Subject)

<<<<<<< HEAD
class Day(Model):
	name = CharField(choices=(('Monday'), ('Tuesday'), ('Wednesday'),
		    ('Thursday'), ('Friday'), ('Saturday'), ('Sunday')))
=======

>>>>>>> 0887f820c0c0919c9a6ead38d9ce2593e73143af
