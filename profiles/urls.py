from django.urls import include, re_path
from django.urls import path
from . import views
import profiles

urlpatterns = [  
     path('',views.profiles_home, name='profiles_home'),
     path('list/',views.profiles_list, name='profiles_list'),     
     path('education/',views.profiles_education, name='profiles_education'),
     path('experience/',views.profiles_experience, name='profiles_experience'), 
     path('achivements/',views.profiles_achivements, name='profiles_achivements')      
	]
