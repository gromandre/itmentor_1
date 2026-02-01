import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def make_session() -> requests.Session:
    """Создаёт настроенную Session: User-Agent + Retry через HTTPAdapter."""
    session = requests.Session()

    # Обязательный User-Agent
    session.headers.update({
        "User-Agent": "weather-cli/1.0 (+https://example.local)"
    })

    # Retry: повторы на временных сбоях/5xx/429
    retry = Retry(
        total=5,
        connect=5,
        read=5,
        status=5,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
        raise_on_status=False,
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session