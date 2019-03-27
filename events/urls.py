# /events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.index, name='events'),		# path for event view
    path('add-event/', views.add_event, name='add_event'),	# path for adding event view		
]