import json
import pandas as pd
from pandas.io.json import json_normalize

with open('city.list.json', 'r', encoding='utf-8') as city_file:
    cities = json.load(city_file)

df = json_normalize(cities)
df.to_csv('cities.csv')

# https://worldpopulationreview.com/world-cities/
# api.openweathermap.org/data/2.5/weather?id=3117735&appid=
# api key 

