from .filters import VolunteerFilter
from .forms import EmailForm
from django.shortcuts import render
import yagmail 
from volunteers.models import Volunteer
from events.models import Event
from users.models import CustomUser

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
        # user = CustomUser.objects.get(email = request.user.email)
        # email = user.email
        email = "julianl18111567@alumni.tas.tw"
        yag = yagmail.SMTP(email, password)
        contents = [
            message
        ]
        yag.send(recipients, subject, contents)
        return render(request, 'emailsuccess.html')



   
