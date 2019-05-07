from django.db import models
from django.utils import timezone # for default time

from volunteers.models import Volunteer

# Create your models here.

class Event(models.Model):		# To store events
 	name = models.CharField(max_length=256)
 	description = models.TextField(default='')
 	address = models.CharField(max_length=256)
 	time = models.DateTimeField(default=timezone.now)	# default is today
 	volunteers = models.ManyToManyField(Volunteer)
 	cost = models.IntegerField(default=1000)	# dollar cost of the event

 	def __str__(self):
 		return self.name
