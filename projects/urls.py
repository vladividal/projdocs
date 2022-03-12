from django.urls import include, re_path
from django.urls import path
from . import views
import projects

urlpatterns = [  
     path('',views.projects_home, name='projects_home')
#     path('education/',views.profiles_education, name='profiles_education'),
#     path('experience/',views.profiles_experience, name='profiles_experience'), 
#     path('achivements/',views.profiles_achivements, name='profiles_achivements')      
	]
