from django import forms
from volunteers.models import Volunteer

class EmailForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(queryset = Volunteer.objects.all())
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(max_length=100)
    