from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
 # return HttpResponse('Home Page')
 return render(request,'index.html')

def contact(request):
 # return HttpResponse('Contact Page')
 return render(request,'contact.html')

def blog(request):
 # return HttpResponse('Blog Page')
 return render(request,'blog.html')

def about(request):
 # return HttpResponse('About Page')
 return render(request,'about.html')

def login(request):
 # return HttpResponse('About Page')
 return render(request,'login.html')