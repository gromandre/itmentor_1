import requests
import logging

def get_geocode_city(city: str) -> dict|None:
    end_point = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
        'name': city,
        'count': 10,
        'language': 'ru',
        'format': 'json',
    }

    response = requests.get(end_point, params=params)
    response.raise_for_status()
    logging.info('Ответ от сервера: ОК {}'.format(response.status_code))

    data = response.json()
    logging.debug(data)
    return data