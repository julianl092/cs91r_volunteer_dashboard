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

def edit_volunteer(request):
	volunteer_id = request.GET.get('id', '')
	if volunteer_id == '':
		return render(request, 'form_error.html')	# error page
	else:
		form_instance = Volunteer.objects.get(id=volunteer_id)
		if request.method == "GET":		# render page to edit event
			form = VolunteerForm(instance=form_instance)
			context = {'form': form}
			return render(request, 'volunteers_edit.html',context)
		elif request.method == "POST":	# edit event data
			if(request.POST.get('delete', '') == ''):		# if not delete
				print(request.POST.get('delete'))
				form = VolunteerForm(request.POST, instance=form_instance)
				if form.is_valid():
					form.save()		# save new event data to form
					volunteers = Volunteer.objects.values()	# get querySet of events
					context = {'volunteers': volunteers} 	
					return render(request, 'volunteers.html', context)		# render events html
				else:
					return render(request, 'form_error.html')	# error page
			else:	# if delete button was clicked
				form_instance.delete()
				volunteers = Volunteer.objects.values()	# get querySet of events
				context = {'volunteers': volunteers} 	
				return render(request, 'volunteers.html', context)		# render events html


