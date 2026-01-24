import json
import os

def save_cache(path: str, cache: dict) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)

def load_cache(path: str) -> dict:
    if not os.path.exists(path):
        return {}

    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)