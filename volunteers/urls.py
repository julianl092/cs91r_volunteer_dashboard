# /volunteers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('volunteers/', views.index, name='volunteers'),		# path for event view
]