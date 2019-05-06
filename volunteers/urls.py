# /volunteers/urls.py

from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path('volunteers/', views.index, name='volunteers'),		# path for volunteer view
    path('add-volunteer/', views.add_volunteer, name='add_volunteer'),	# path for adding volunteer view
    path('edit-volunteer/', views.edit_volunteer, name='edit_volunteer'),	# path for editing volunteer view
    # path('upload-csv/', views.upload_csv, name='upload_csv'),
    re_path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
]