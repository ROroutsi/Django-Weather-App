from django.forms import ModelForm, TextInput
from .models import city

class CityForm(ModelForm):
    class Meta:
        model = city
        fields = ['city_name']
        widgets = {
            'city_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }