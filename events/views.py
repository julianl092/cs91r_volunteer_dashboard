from django.shortcuts import render
from .models import Event
from .forms import EventForm

def index(request):
	if request.method == "GET":
		events = Event.objects.all()	# get querySet of events
		context = {'events': events} 	
		return render(request, 'events.html', context)		# render events html

	elif request.method == "POST":
		print("POST request")

def filter_events(request):
	if request.method == "GET":		# render page with form to filter events
		context = {
		
		}
		return render(request, 'filter_events.html', context)

	elif request.method == "POST":	# return filtered events page
		events = Event.objects.values()	# get querySet of events
		context = {
			'events': events
		} 	
		return render(request, 'events.html', context)

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
			events = Event.objects.all()	# get querySet of events
			context = {'events': events} 	
			return render(request, 'events.html', context)		# render events html
		else:
			return render(request, 'form_error.html')	# error page

def edit_event(request):
	event_id = request.GET.get('id', '')
	if event_id == '':
		return render(request, 'form_error.html')	# error page
	else:
		form_instance = Event.objects.get(id=event_id)
		if request.method == "GET":		# render page to edit event
			form = EventForm(instance=form_instance)
			context = {'form': form}
			return render(request, 'events_edit.html',context)
		elif request.method == "POST":	# edit event data
			if(request.POST.get('delete', '') == ''):		# if not delete
				form = EventForm(request.POST, instance=form_instance)
				if form.is_valid():
					form.save()		# save new event data to form
					events = Event.objects.all()	# get querySet of events
					context = {'events': events} 	
					return render(request, 'events.html', context)		# render events html
				else:
					return render(request, 'form_error.html')	# error page
			else:	# if delete button was clicked
				form_instance.delete()
				events = Event.objects.all()	# get querySet of events
				context = {'events': events} 	
				return render(request, 'events.html', context)		# render events html
