# volunteers/forms.py

from django import forms
from volunteers.models import Volunteer 

class VolunteerForm(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = (
			'name',
			'address',
			'birthday',
			'gender',
			'email',
		)