from .filters import VolunteerFilter
from .forms import EmailForm
from django.shortcuts import render
import yagmail 
from volunteers.models import Volunteer
from events.models import Event
from users.models import CustomUser
from django.http import HttpResponse
from time import strftime

def search(request):
    user_list = Volunteer.objects.all()
    user_filter = VolunteerFilter(request.GET, queryset=user_list)
    if request.method == 'GET':
        return render(request, 'emails.html', {'filter': user_filter, 'form': EmailForm})
    elif request.method == 'POST': 
        form = EmailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("message")
            subject = form.cleaned_data.get('subject')
            password = form.cleaned_data.get('password')
            recipients = [vol.email for vol in list (user_filter.qs)]
        email = "julianl18111567@alumni.tas.tw"
        yag = yagmail.SMTP(email, password)
        contents = [
            message
        ]
        yag.send(recipients, subject, contents)
        return render(request, 'emailsuccess.html')

def remind (request, id): 
    event = Event.objects.filter(pk=id)[0]
    user_list = event.volunteers
    user_filter = VolunteerFilter(request.GET, queryset=user_list)
    popform = EmailForm({'subject': 'Event Reminder', 'message':  "Dear volunteer - please remember that you've signed up for " + event.name + " to be hosted at" + str(event.time) + "! Looking forward to seeing you there."})
    return render (request, 'emails.html', {'filter': user_filter, 'form': popform})

def customsend (request, email, name): 
    user_list = Volunteer.objects.filter(name = name)
    user_filter = VolunteerFilter(request.GET, queryset=user_list)
    popform = EmailForm({'subject': 'Welcome to the Campaign!', 'message':  "Dear" + name + ", thank you for registering to volunteer for our political campaign! We've got a ton of incredible events coming up, and we'll need all the help we can get. We'll follow up with details soon, but in the meantime, welcome onboard!"})
    return render (request, 'emails.html', {'filter': user_filter, 'form': popform})

def quicksend (request, email, name):
    sender = "julianl18111567@alumni.tas.tw"
    password = "austinhuang"
    subject = "Welcome to the Campaign!"
    message = "Dear" + name + ", thank you for registering to volunteer for our political campaign! We've got a ton of incredible events coming up, and we'll need all the help we can get. We'll follow up with details soon, but in the meantime, welcome onboard!"
    yag = yagmail.SMTP(sender, password)
    contents = [
        message
    ]
    yag.send(email, subject, contents)
    return render(request, 'emailsuccess.html')




   
