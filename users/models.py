# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return self.email