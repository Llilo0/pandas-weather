# z pliku config.py zaimportuj Settings
from http.client import responses

from config import Settings
import requests
from datetime import datetime


def fetch_weather ():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": weather["main"]["feels_like"],
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": weather["main"]["temp"],
            "Opis pogody": weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkosc wiatru": weather["wind"]["speed"],
            "Data pomiaru": datetime.now()
        }
        return data

    except Exception as e:
        print("Wystąpił błąd:", e)
