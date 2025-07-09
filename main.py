from api import fetch_weather
from excel import append_to_excel, append_to_csv

import time

while True:
    data = fetch_weather()

    append_to_excel(data)
    append_to_csv(data)

    time.sleep(10)
    print("Pobrano nowe dane")



