import logging

def setup_logging(path: str = 'weather.log') -> None:
    logging.basicConfig(
        filename='weather.log',
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s',
        encoding='utf-8'
    )
