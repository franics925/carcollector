# Generated by Django 2.2.3 on 2019-09-11 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_car_mileage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='car',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='details',
        ),
    ]
