import json
import os
import logging

def save_cache(path: str, cache: dict) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)

def load_cache(path: str) -> dict:
    if not os.path.exists(path):
        logging.info('Кэш-файл не найден, создаю новый')
        return {}

    if os.path.getsize(path) == 0:
        logging.info('Кэш-файл пустой')
        return {}

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.warning('Кэш-файл повреждён, сбрасываю')
        return {}