# Generated by Django 2.2.3 on 2019-09-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='main_app.Car'),
        ),
    ]
