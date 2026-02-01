import requests
import logging

def get_temp(session: requests.Session, lat: float, lon: float) -> dict | None:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "current": "temperature_2m",
        "timezone": "auto",
        "past_days": 0,
        "forecast_hours": 24,
    }

    try:
        response = session.get(url, params=params, timeout=(5, 20))
        response.raise_for_status()
        logging.info("Forecast: OK %s (lat=%s lon=%s)", response.status_code, lat, lon)
        return response.json()

    except requests.exceptions.Timeout:
        logging.error("Forecast: таймаут (lat=%s lon=%s)", lat, lon)
        return None

    except requests.exceptions.HTTPError as e:
        logging.error("Forecast: HTTP ошибка (lat=%s lon=%s): %s", lat, lon, e)
        return None

    except requests.exceptions.RequestException as e:
        logging.error("Forecast: сетевая ошибка (lat=%s lon=%s): %s", lat, lon, e)
        return None