from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Maintenance(models.Model):
    date = models.DateField()
    mnType = models.CharField(
        max_length=1,
        choices=MNTYPES,
        default=MNTYPES[0][0]
    )
    details = models.CharField(max_length=200)
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_maintenance_desplay()} on {self.date}"