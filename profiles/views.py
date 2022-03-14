from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def profiles_home(request):
     return render(request, 'profiles/profiles_home.html')

def profiles_list(request):
     lista_profiles = Profile.objects.all()
     return render(request, 'profiles/profiles_list.html',{"profiles":lista_profiles})

def profiles_education(request):
     return render(request, 'profiles/profiles_education.html')    

def profiles_experience(request):
     return render(request, 'profiles/profiles_experience.html') 

def profiles_achivements(request):
     return render(request, 'profiles/profiles_achivements.html')     