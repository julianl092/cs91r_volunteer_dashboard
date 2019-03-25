from django.db import models
from django.utils import timezone # for default time

import volunteers # import volunteers app

# Create your models here.

class Event(models.Model):		# To store events
 	name = models.CharField(max_length=256)
 	description = models.TextField(default='')
 	address = models.CharField(max_length=256)
 	time = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7))	# default a week from current
 	volunteers = models.ManyToManyField(	# joins events and volunteers
 		'volunteers.Volunteer',
 		related_name='events_volunteers',
 		blank=True,
 	)

 	def __str__(self):
 		return self.name
