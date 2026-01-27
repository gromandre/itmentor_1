
from cache_store import load_cache, save_cache
import logging
from logconf import setup_logging
from geocode_city import get_geocode_city
from get_temps import get_temp
from save_forecast import save_forecast

CACHE_FILE = 'cache_geo.json'
def main():
    setup_logging()
    logging.info('Старт скрипта')

    cities = ['volgograd', 'moskva']

    for city in cities:
        city = city.lower()


        cache = load_cache(CACHE_FILE)
        logging.info('Загрузил кэш')

        if city in cache:
            logging.info('Нашел город {} в кэше'.format(city))

        else:
            try:
                logging.info('Города {} в кэше нет, делаю запрос на сервер'.format(city))
                data = get_geocode_city(city)
                results = data.get('results')

                if not results:
                    logging.error(f'Город {city} не найден')
                else:
                    first = results[0]
                    cache[city] = {"lat": first['latitude'], "lon": first['longitude']}

                    logging.info('Делаю запрос на сервер, чтобы по координатам получить почасовой прогноз на ближайшие 24 часа')
                    res = get_temp(cache[city]["lat"], cache[city]["lon"])
                    logging.debug(res)
                    hours = res["hourly"]["time"]
                    temps = res["hourly"]["temperature_2m"]
                    info_temps = list(zip(hours, temps))
                    cache[city]['current_time'] = res['current']['time']
                    cache[city]['info_temps'] = info_temps



                    save_cache(CACHE_FILE, cache)
                    logging.info('Город {} cохранен в кэш'.format(city))

                    logging.debug('Запрашиваю температуру')



            except Exception as e:
                logging.error(e)

        save_forecast(cache)

if __name__ == "__main__":
    main()
