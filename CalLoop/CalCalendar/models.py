from django.db.models import *

# Create your models here.
class Subject(Model):
	name = CharField()
	weekday = ManyToManyField(Day)


class Assignment(Model):
	name = CharField()
	due_date = DateTimeField()
	due_in = DurationField()
	subject = ForeignKey(Subject)

class Day(Model):
	name = CharField(choices=(('Monday'), ('Tuesday'), ('Wednesday'),
		    ('Thursday'),) ('Friday'), ('Saturday'), ('Sunday'))
