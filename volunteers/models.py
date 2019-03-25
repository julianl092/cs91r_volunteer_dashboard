from django.db import models
from django.utils import timezone # for time


# Create your models here.

class Volunteer(models.Model):		# To store events
 	name = models.CharField(max_length=256)
 	address = models.CharField(max_length=256)
 	birthday = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7))	# default a week from current
 	gender = models.CharField(max_length=16)
 	email = models.EmailField()

 	def __str__(self):
 		return self.name
