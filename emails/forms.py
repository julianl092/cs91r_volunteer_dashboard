from django import forms
from volunteers.models import Volunteer

class EmailForm(forms.Form):
    subject = forms.CharField(widget = forms.Textarea(attrs={'style': 'height: 100px; width: 100%;'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'style': 'height: 400px; width: 100%;'}))
    password = forms.CharField(max_length=100)
    