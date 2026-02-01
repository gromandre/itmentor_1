import requests
import logging

def get_geocode_city(session: requests.Session, city: str) -> dict|None:
    end_point = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
        'name': city,
        'count': 10,
        'language': 'ru',
        'format': 'json',
    }

    try:
    # timeout
        response = session.get(end_point, params=params, timeout=(5, 20))
        response.raise_for_status()
        logging.info("Геокодер: OK %s (%s)", response.status_code, city)
        return response.json()

    except requests.exceptions.Timeout:
        logging.error("Геокодер: таймаут (%s)", city)
        return None

    except requests.exceptions.HTTPError as e:
        logging.error("Геокодер: HTTP ошибка (%s): %s", city, e)
        return None

    except requests.exceptions.RequestException as e:
        logging.error("Геокодер: сетевая ошибка (%s): %s", city, e)
        return None