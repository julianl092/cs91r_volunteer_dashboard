from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'emails'
urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    path('<str:email>/<str:name>/', views.quicksend, name='quicksend'),
]