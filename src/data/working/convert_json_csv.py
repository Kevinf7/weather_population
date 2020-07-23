import json
import pandas as pd
from pandas.io.json import json_normalize

with open('city.list.json', 'r', encoding='utf-8') as city_file:
    cities = json.load(city_file)

df = json_normalize(cities)
df.to_csv('cities.csv')



