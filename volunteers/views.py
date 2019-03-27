from django.shortcuts import render
from .models import Volunteer
from .forms import VolunteerForm

def index(request):
	if request.method == "GET":
		volunteers = Volunteer.objects.values()
		context = {
			'volunteers': volunteers,
		}
		return render(request, 'volunteers.html', context)

	elif request.method == "POST":
		print("POST request volunteer")

def add_volunteer(request):
	if request.method == "GET":		# render page with form to add new event
		form = VolunteerForm()
		context = {
			'form': form
		}
		return render(request, 'volunteers_add.html', context)	# render events_add.html

	elif request.method == "POST":	# save the form input as new event in database
		form = VolunteerForm(request.POST)
		if form.is_valid():
			form.save()		# save new event data to form
			volunteers = Volunteer.objects.values()	# get querySet of events
			context = {'volunteers': volunteers} 	
			return render(request, 'volunteers.html', context)		# render events html
		else:
			return render(request, 'form_error.html')	# error page