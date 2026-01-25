import os
import csv

def save_forecast(cache):
    with open("forecast.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "city",
            "current_time",
            "min_temp",
            "max_temp",
            "avg_temp",
        ])

        for city, current in cache.items():
            temps = [t for _, t in current["info_temps"]]

            if not temps:
                continue

            t_min = min(temps)
            t_max = max(temps)
            t_avg = sum(temps) / len(temps)

            writer.writerow([
                city,
                current["current_time"],
                t_min,
                t_max,
                round(t_avg, 2),
            ])
