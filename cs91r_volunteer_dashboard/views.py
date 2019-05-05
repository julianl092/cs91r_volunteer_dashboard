from django.shortcuts import render
from volunteers.models import Volunteer
from events.models import Event
from geopy.geocoders import Nominatim
import csv

def home(request): 
	vols = Volunteer.objects.all()
	# Find latitude, longitude for each address
	coords = []
	for volunteer in vols.values():
		name = volunteer['name']
		address = volunteer['address']
		geolocator = Nominatim()
		location = geolocator.geocode(address)
		coords.append([location.latitude, location.longitude, name])
	# Redo csv file for geo addresses
	filename = "static/js/airport.csv"
	with open("static/js/airport.csv", "w+") as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(coords)

	evs = Event.objects.all()
	return render (request, 'home.html', context = {"volunteers": vols[:4], "events": evs[:4]})