from django.shortcuts import render
from django.http import HttpResponse

def profiles_home(request):
     return render(request, 'profiles/profiles_home.html')
#    return HttpResponse('Profiles Home')

def profiles_education(request):
     return render(request, 'profiles/profiles_education.html')    

def profiles_experience(request):
     return render(request, 'profiles/profiles_experience.html') 

def profiles_achivements(request):
     return render(request, 'profiles/profiles_achivements.html')     