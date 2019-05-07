from django.db import models
from django.utils import timezone 	# for time
# from events.models import Event 	# link to event
from django.core.validators import MinValueValidator, MaxValueValidator	# constrain numbers


# Create your models here.

class Volunteer(models.Model):		# To store volunteers
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

class VolunteerReport(models.Model):		# To store reports from volunteers
	volunteer = models.ForeignKey(
		'volunteers.Volunteer',
		on_delete=models.CASCADE,
	)
	event = models.ManyToManyField('events.Event')
	comments = models.TextField(
		blank=True,
		max_length=3600,
	)
	# Ratings on a scale of 1 to 10
	overall_rating = models.PositiveIntegerField(
		default=5,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(10),
		]
	)
	satisfaction = models.PositiveIntegerField(
		default=5,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(10),
		]
	)
	support = models.PositiveIntegerField(
		default=5,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(10),
		]
	)
	meaningful = models.PositiveIntegerField(
		default=5,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(10),
		]
	)
	repeat_likeliness = models.PositiveIntegerField(
		default=5,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(10),
		]
	)