from django.shortcuts import render
from django.http import HttpResponse

def projects_home(request):
     return render(request, 'projects/projects_home.html')

#def profiles_education(request):
#     return render(request, 'profiles/profiles_education.html')    

#def profiles_experience(request):
#     return render(request, 'profiles/profiles_experience.html') 

#def profiles_achivements(request):
#     return render(request, 'profiles/profiles_achivements.html')  
