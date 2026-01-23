import requests
import json
import os
import logging

logging.basicConfig(
    filename='weather.log',
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

CACHE_FILE = 'cache_geo.json'

def save_cache(cache: dict) -> None:
    with open(CACHE_FILE, 'w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)

def load_cache() -> dict:
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

logging.info('Старт скрипта')

city = 'Abakan'
city = city.lower()
end_point = 'https://geocoding-api.open-meteo.com/v1/search'
params = {
    'name': city,
    'count': 10,
    'language': 'en',
    'format': 'json',
}

cache = load_cache()
logging.info('Загрузил кэш')

if city in cache:
    logging.info('Нашел город {} в кэше'.format(city))
    print(cache[city])
else:
    try:
        logging.info('Города {} в кэше нет, делаю запрос на сервер'.format(city))
        response = requests.get(end_point, params=params)
        response.raise_for_status()
        logging.info('Ответ от сервера: ОК {}'.format(response.status_code))

        data = response.json()
        logging.debug(data)

        results = data.get('results')
        if not results:
            logging.error(f'Город {city} не найден')
        else:
            first = results[0]
            cache[city] = {"lat": first['latitude'], "lon": first['longitude']}
            save_cache(cache)
            logging.info('Город {} cохранен в кэш'.format(city))

    except Exception as e:
        logging.error(e)


