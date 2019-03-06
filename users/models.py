# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	# add additional fields here

	def __str__(self):
		return self.email