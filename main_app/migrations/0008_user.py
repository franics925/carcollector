# Generated by Django 2.2.3 on 2019-09-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20190911_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
