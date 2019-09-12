from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

MNTYPES = (
    ('C', 'Checkup'),
    ('O', 'Oil Change'),
    ('R', 'Repair')
)

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()
    # drivers = models.ManyToManyField(Driver)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.model
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Driver(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    cars = models.ManyToManyField(Car)
    def __str__(self):
        return self.name

class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')
    mnType = models.CharField(
        max_length=1,
        choices=MNTYPES,
        default=MNTYPES[0][0]
    )
    details = models.CharField(max_length=200)
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_mnType_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"