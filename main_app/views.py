from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

import uuid
import boto3

from .models import *
from .forms import *

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'carcollec'

# Create your views here.

def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def driver_index(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'maintenance_form': maintenance_form 
    })

def add_maintenance(request, car_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.car_id = car_id
    new_maintenance.save()
  return redirect('detail', car_id=car_id)

def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except:
            print('An error occured uploading file to s3')
    return redirect('detail', car_id=car_id)

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'
