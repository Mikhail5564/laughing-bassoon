import requests


def get_weather(city):
    city = city.strip()
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        'name': city,
        'count': 1,
        'language': 'ru',
        'format': 'json'
    }

    try:
        response = requests.get(url=geo_url, params=geo_params)
        geo_info = response.json()
        if "results" in geo_info:
            latitude = geo_info["results"][0]['latitude']
            longitude = geo_info["results"][0]['longitude']
            citynormal = geo_info["results"][0]["name"]
            weather_url = "https://api.open-meteo.com/v1/forecast"
            weather_params = {
                'latitude': latitude,
                'longitude': longitude,
                'current_weather': 'true',
                'timezone': 'auto',
                'forecast_days': 1
            }
            responce_weather = requests.get(url=weather_url, params=weather_params)
            responce_weather_info = responce_weather.json()
            temperature = responce_weather_info["current_weather"]["temperature"]
            wind_speed = responce_weather_info["current_weather"]["windspeed"]
            t = responce_weather_info['current_weather_units']['temperature']
            ws = responce_weather_info['current_weather_units']["windspeed"]
            return {"weather": f"Температура в городе {citynormal} на данный момент составляет {temperature} {t}, а также скорость ветра"
                    f" вашего города составляет {wind_speed} {ws}"}
    except Exception as error:
        return {"error": f"Ошибка. Код ошибки {error}"}