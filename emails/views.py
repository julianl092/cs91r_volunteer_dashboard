from django.shortcuts import render
import yagmail 
from volunteers.models import Volunteer
from .forms import EmailForm
from users.models import CustomUser

def index(request): 
    context = {'volunteers': Volunteer.objects.all(), 'form': EmailForm}
    if request.method == 'GET': 
        return render (request, 'emails.html', context)
    elif request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipients = []
            volunteers = form.cleaned_data.get("recipients")
            message = form.cleaned_data.get("message")
            subject = form.cleaned_data.get('subject')
            password = form.cleaned_data.get('password')
            for volunteer in volunteers: 
                recipients.append(volunteer.email)
        user = CustomUser.objects.get(email = request.user.email)
        email = user.email
        yag = yagmail.SMTP(email, password)
        contents = [
            message
        ]
        yag.send(recipients, subject, contents)
    return render(request, 'emails.html',context)
