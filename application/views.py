from django.shortcuts import render
from .models import Profile

# Create your views here.
def profileHome(request):
    profile = Profile.objects.all().first()
    context = {
        # 'name':'Ige Tolulope'
        'name':profile.name,
        'location':profile.address,
        # occupation, work_place
        'occupation':profile.occupation,
        'workplace':profile.workplace,
        'linkedIn':profile.linkedIn_link,
        # work_place = SQI College of ICT, Ibadan (On-line) 
        # 'name':profile.name,
    }
    return render(request, 'profile.html', context)