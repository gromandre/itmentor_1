import requests

def get_temp(lat: float, lon: float):
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
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()
    return data