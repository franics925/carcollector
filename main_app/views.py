from django.shortcuts import render,redirect
from .models import *

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car(request):
    return HttpResponse('<h1>Car Details</h1?')