# volunteers/forms.py

from django import forms
from events.models import Event
from volunteers.models import Volunteer, VolunteerReport

class VolunteerForm(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = (
			'name',
			'address',
			'birthday',
			'gender',
			'email',
			'date_joined',
			'num_hours',
			'num_events',
		)

class ReportForm(forms.ModelForm):
	class Meta:
		model = VolunteerReport
		fields = (
			'volunteer',
			'event',
			'comments',
			'overall_rating',
			'satisfaction',
			'support',
			'meaningful',
			'repeat_likeliness',
		)
