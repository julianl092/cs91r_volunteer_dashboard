from django.db import models
from users.models import CustomUser

class Event (models.Model): 
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    location =  models.CharField(
        max_length=200, blank=False, null=False, default=''
    )
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    participants = models.ManyToManyField(
        CustomUser
    )

class Task(models.Model):  
    description = models.TextField()
    completed = models.BooleanField()   
    due_date = models.DateTimeField()
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    assigned_to = created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
    )
        null=True,
    )
    
