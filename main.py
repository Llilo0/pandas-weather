from api import fetch_weather
from excel import append_to_excel

data = fetch_weather()

append_to_excel(data)



