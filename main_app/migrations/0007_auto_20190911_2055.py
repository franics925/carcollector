# Generated by Django 2.2.3 on 2019-09-11 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20190911_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='Maintenance Date'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Car')),
            ],
        ),
    ]