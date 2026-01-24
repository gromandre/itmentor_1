import logging

def setup_logging(path: str = 'weather.log') -> None:
    logging.basicConfig(
        filename=path,
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(message)s',
        encoding='utf-8'
    )