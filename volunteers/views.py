from django.shortcuts import render
from .models import Volunteer
from .forms import VolunteerForm

def index(request):
	if request.method == "GET":
		print("GET request volunteer")
		volunteers = Volunteer.objects.values()
		context = {
			'volunteers': volunteers,
		}
		return render(request, 'volunteers.html', context)

	elif request.method == "POST":
		print("POST request volunteer")