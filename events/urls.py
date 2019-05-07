# /events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.index, name='events'),		# path for event view
    path('filter-events/', views.filter_events, name='filter_events'),	# path for filtering events view
    path('add-event/', views.add_event, name='add_event'),	# path for adding event view		
    path('edit-event/', views.edit_event, name='edit_event'),	# path for editing event view
]