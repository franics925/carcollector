from django.forms import ModelForm
from .models import *

class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'mnType', 'details', 'cost']