from django.shortcuts import render
from volunteers.models import Volunteer
from events.models import Event

def home(request): 
    vols = Volunteer.objects.all().order_by('-date_joined')[:4]
    evs = Event.objects.all()[:4]
    return render (request, 'home.html', context = {"volunteers": vols, "events": evs})