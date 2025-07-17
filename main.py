from api import fetch_weather
from excel import append_to_excel, append_to_csv
from database import add_record
import time

while True:
    data = fetch_weather()

    append_to_excel(data)
    append_to_csv(data)

    add_record(data)

    time.sleep(30)
    print("Pobrano nowe dane")



