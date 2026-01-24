import requests
from cache_store import load_cache, save_cache
import logging
from logconf import setup_logging

CACHE_FILE = 'cache_geo.json'
def main():
    setup_logging()
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

    cache = load_cache(CACHE_FILE)
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
                save_cache(CACHE_FILE, cache)
                logging.info('Город {} cохранен в кэш'.format(city))

        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    main()
