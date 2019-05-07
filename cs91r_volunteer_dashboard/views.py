from django.shortcuts import render
from volunteers.models import Volunteer
from events.models import Event
from geopy.geocoders import Nominatim
import csv, json
import string
from datetime import datetime
from geojson import Feature, FeatureCollection, Point

def home(request): 
	vols = Volunteer.objects.all()
	# Find latitude, longitude for each address
	features = []
	for volunteer in vols.values():
		name = volunteer['name']
		address = volunteer['address']
		geolocator = Nominatim()
		try:
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
		except:
			print(geolocator.geocode(address))
		
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
	return render (request, 'home.html', context = {"volunteers": vols[:4], "events": evs[:2]})

def analytics(request):
	vols = Volunteer.objects.all()
	evs = Event.objects.all()
	vols_ages = []
	# Current time
	today = datetime.today()
	curr_year = today.year 
	curr_month = today.month 
	curr_day = today.day 
	for vol in vols.values():
		vol_year = vol['birthday'].year
		vol_month = vol['birthday'].month
		vol_day = vol['birthday'].day
		age = curr_year - vol_year
		if curr_month < vol_month:
			age -= 1
		elif curr_month == vol_month and curr_day < vol_day:
			age -= 1
		vols_ages.append(age)
	
	# Write to json
	with open("static/js/ages.json", "w+") as f:
		json.dump(vols_ages, f)

	context = {
		'volunteers': vols,
		'events': evs,
	}
	return render(request, 'analytics.html', context = context)
