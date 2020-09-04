from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9cb1eb38e08f967c8af841bec68be827'
    city='mumbai'
    r = requests.get(url.format(city)).json()
    print(r)
    city_weather = {
                'city' : city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                }
    context={'city_weather':city_weather}

    return render(request,'weather/weather.html',context)