from django.shortcuts import render
from volunteers.models import Volunteer
from events.models import Event
from geopy.geocoders import Nominatim
import csv, json
import string
from geojson import Feature, FeatureCollection, Point

def home(request): 
	vols = Volunteer.objects.all()
	# Find latitude, longitude for each address
	features = []
	for volunteer in vols.values():
		name = volunteer['name']
		address = volunteer['address']
		geolocator = Nominatim()
		location = geolocator.geocode(address)
		latitude, longitude = map(float, (location.latitude, location.longitude))
		features.append(
			Feature(
				geometry = Point((longitude, latitude)),
				properties = {
					'name': name,
				}
			)
		)

	evs = Event.objects.all()
	for event in evs.values():
		name = event['name']
		address = event['address']
		geolocator = Nominatim()
		location = geolocator.geocode(address)
		if location:
			latitude, longitude = map(float, (location.latitude, location.longitude))
			features.append(
				Feature(
					geometry = Point((longitude, latitude)),
					properties = {
						'name': name,
					}
				)
			)

	# Write to json
	collection = FeatureCollection(features)
	with open("static/js/data.geojson", "w+") as f:
		f.write('%s' % collection)
	return render (request, 'home.html', context = {"volunteers": vols[:4], "events": evs[:4]})
