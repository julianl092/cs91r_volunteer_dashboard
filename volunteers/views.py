from django.shortcuts import render
from .models import Volunteer
from .forms import VolunteerForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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
		print(request.POST)
		if form.is_valid():
			form.save()		# save new event data to form
			volunteers = Volunteer.objects.values()	# get querySet of events
			context = {'volunteers': volunteers} 	
			return render(request, 'volunteers.html', context)		# render events html
		else:
			return render(request, 'form_error.html')	# error page

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		form = VolunteerForm()
		context = {
			'form': form
		}
		return render(request, 'volunteers_add.html', context)	
    # if not GET, then proceed
	try:
		print(request.FILES)
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("upload_csv"))

		file_data = csv_file.read().decode("utf-8")		

		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		lines.pop(0) #removes namesc
		for indx, line in enumerate(lines):	
			print(line)
			fields = line.split(",")
			data_dict = {}
			data_dict["name"] = fields[0]
			data_dict["address"] = fields[1]
			data_dict["initial-birthday"] = fields[1]
			data_dict["birthday"] = fields[2]
			data_dict["gender"] = fields[3]
			data_dict["email"] = fields[4]
			data_dict["date_joined"] = fields[5]
			data_dict["initial-date_joined"] = fields[5]
			data_dict["num_hours"] = fields[6]
			data_dict["num_events"] = fields[7]
			# print("data:")
			# print(data_dict)
			try:
				form = VolunteerForm(data_dict)
				if form.is_valid():
					form.save()	
					volunteers = Volunteer.objects.values()	# get querySet of events
					context = {'volunteers': volunteers} 	
					if(indx == len(lines) -1):
							return render(request, 'volunteers.html', context)		# render events html
					# return render(request, 'volunteers.html', context)					
				else:
					return render(request, 'form_error.html')	# error page
			except Exception as e:
				print("error")			
				print(e)		
				pass
				return render(request, 'form_error.html')	# error page

	except Exception as e:
		print("error")			
		print(e)
		return render(request, 'form_error.html')	# error page		
	
	return HttpResponseRedirect(reverse("upload_csv"))

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


