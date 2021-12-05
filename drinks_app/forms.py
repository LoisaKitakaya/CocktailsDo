from django import forms
from django.db.models import fields
from .models import DrinksData

# form class
class DrinkForm(forms.ModelForm):

    class Meta:
        model = DrinksData
        fields = '__all__'
