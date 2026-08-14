import requests


def get_currency(currency):
    """Получение курса с помощью бесплатного API"""
    url = f"https://api.exchangerate-api.com/v4/latest/{currency.upper()}"
    try:
        response = requests.get(url)
        data = response.json()
        # Извлекаем курс рубля к доллару
        rub_rate = data['rates']['RUB']  # [citation:5][citation:8]
        return rub_rate
    except Exception as e:
        print(f"Ошибка получения курса: {e}")
        return 75.0  # Запасной курс
