import requests
import json
import os

CACHE_FILE = 'cache_geo.json'

def save_cache(cache: dict) -> None:
    with open(CACHE_FILE, 'w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)

def load_cache() -> dict:
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


city = 'Volgograd'
r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json')
print(r.text)

# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&timezone=auto&past_days=1&forecast_days=1