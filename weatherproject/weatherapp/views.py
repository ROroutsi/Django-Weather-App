from django.shortcuts import render
import requests
from .models import city
from .forms import CityForm

# Create your views here.

def index(request):
	

	api = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOURAPICODE'

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	
	form = CityForm()

	cities = city.objects.all()

	city_data = []

	for c in cities:	
		city_weather = requests.get(api.format(c)).json()
		celsius = round((city_weather['main']['temp'] - 32)* 5/9)
		weather = {
			'city' : c,
	        'temperature' : celsius,
	        'description' : city_weather['weather'][0]['description'],
	        'icon' : city_weather['weather'][0]['icon']
	        }
		city_data.append(weather)

	information = { 'city_data': city_data, 'form': form }
	
	return render(request, 'weatherapp/base.html', information)

    

