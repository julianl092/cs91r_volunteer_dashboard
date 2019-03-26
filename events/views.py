from django.shortcuts import render
from .models import Event
from .forms import EventForm

def index(request):
	if request.method == "GET":
		events = Event.objects.values()	# get querySet of events
		context = {'events': events} 	
		return render(request, 'events.html', context)		# render events html

	elif request.method == "POST":
		print("POST request")