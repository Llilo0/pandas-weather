from api import fetch_weather
from excel import append_to_excel
import time

while True:
    data = fetch_weather()

    append_to_excel(data)

    time.sleep(45)
    print("Pobrano nowe dane")

