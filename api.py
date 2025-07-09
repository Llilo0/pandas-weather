from config import Settings
import requests
from datetime import datetime
from tools import wind_speed
from tools import temp_converter



def fetch_weather ():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": temp_converter(weather["main"]["feels_like"]),
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": temp_converter(weather["main"]["temp"]),
            "Opis pogody": weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkosc wiatru": wind_speed(weather["wind"]["speed"]),
            "Data pomiaru": datetime.now()
        }

        return data

    except Exception as e:
        print("Wystąpił błąd:", e)

print(fetch_weather())