import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Weather CLI utility"
    )

    # Позиционные аргументы — список городов
    parser.add_argument(
        "cities",
        nargs="*",
        help="List of cities (e.g. Moscow Tula)"
    )

    # Опциональный аргумент --file
    parser.add_argument(
        "--file",
        "-f",
        type=Path,
        help="File with list of cities (one per line)"
    )

    return parser.parse_args()


def load_cities(args):
    cities = []

    # 1. Если передан файл
    if args.file:
        if not args.file.exists():
            raise FileNotFoundError(f"File not found: {args.file}")

        with args.file.open(encoding="utf-8") as f:
            for line in f:
                city = line.strip()
                if city and not city.startswith("#"):
                    cities.append(city)

    # 2. Если переданы города через CLI
    if args.cities:
        cities.extend(args.cities)

    if not cities:
        raise ValueError("No cities provided")

    return cities