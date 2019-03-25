# /events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.index, name='events'),		# path for event view
]