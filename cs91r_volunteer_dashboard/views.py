from django.shortcuts import render
from volunteers.models import Volunteer
from events.models import Event

def home(request): 
    vols = Volunteer.objects.all()
    evs = Event.objects.all()
    return render (request, 'home.html', context = {"volunteers": vols[:4], "events": evs[:4]})