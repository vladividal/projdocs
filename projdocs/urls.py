from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     path('',views.home, name='home'),
     path('about/',views.about, name='about'),
     path('blog/',views.blog, name='blog'),
     path('contact/',views.contact, name='contact'),
     path('admin/', admin.site.urls),
     path('profiles/', include('profiles.urls')),
     path('projects/', include('projects.urls'))     
]

urlpatterns += staticfiles_urlpatterns()


