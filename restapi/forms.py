from dataclasses import fields
from django.forms import ModelForm

from restapi.models import DrinkModel

class DrinkForm(ModelForm):
    class Meta:
        model = DrinkModel
        fields = ['name','desc','price']