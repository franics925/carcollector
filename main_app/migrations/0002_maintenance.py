# Generated by Django 2.2.3 on 2019-09-11 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mnType', models.CharField(choices=[('C', 'Checkup'), ('O', 'Oil Change'), ('R', 'Repair')], default='C', max_length=1)),
                ('details', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Car')),
            ],
        ),
    ]
