# Generated by Django 2.2.3 on 2019-09-12 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_user_cars'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Driver',
        ),
    ]
