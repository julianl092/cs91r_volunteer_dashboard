from django.db import models
from django.utils import timezone # for time


# Create your models here.

class Volunteer(models.Model):		# To store events
 	name = models.CharField(max_length=256)
 	address = models.CharField(max_length=256)
 	birthday = models.DateTimeField(default=timezone.now)	# default is today
 	gender = models.CharField(max_length=16)
 	email = models.EmailField()
 	date_joined = models.DateTimeField(default=timezone.now)  # keeps track of when they joined
 	num_hours = models.IntegerField(default=0)
 	num_events = models.IntegerField(default=0)

 	def __str__(self):
 		return self.name
