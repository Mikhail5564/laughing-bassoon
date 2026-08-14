from django.shortcuts import render
from .utils import get_weather


def weather(request):
    if request.method == "GET":
        return render(request, 'weather.html')
    else:
        city = request.POST.get('city', "Москва")
        print(city)
        return render(request, 'weather.html', context=get_weather(city))
