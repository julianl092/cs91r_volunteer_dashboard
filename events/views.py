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

def add_event(request):
	if request.method == "GET":		# render page with form to add new event
		form = EventForm()
		context = {
			'form': form
		}
		return render(request, 'events_add.html', context)	# render events_add.html

	elif request.method == "POST":	# save the form input as new event in database
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()		# save new event data to form
			events = Event.objects.values()	# get querySet of events
			context = {'events': events} 	
			return render(request, 'events.html', context)		# render events html
		else:
			return render(request, 'form_error.html')	# error page


