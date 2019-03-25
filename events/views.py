from django.shortcuts import render
from .models import Event
from .forms import EventForm

def index(request):
	if request.method == "GET":
		print("GET request")

	elif request.method == "POST":
		print("POST request")