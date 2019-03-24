# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):		# Form for creating staff user accounts
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):			# Changing profile for staff user accounts
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')