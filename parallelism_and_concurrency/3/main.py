import requests
import asyncio
import threading

lock = threading.Lock()

def get_status_code(url):
    r = requests.get(url=url)
    with lock:
        with open("status_code.txt", "a") as f:
            f.write(f'{url[8:].replace("/", "")}: {r.status_code}\n')

async def run_get_status_code(sem, url):
    async with sem:
        await asyncio.to_thread(get_status_code, url)

async def main():
    URL = 'https://example.com/'
    requests_amount = 50
    requests_limit = 10

    sem = asyncio.Semaphore(requests_limit)

    tasks = [run_get_status_code(sem, URL) for _ in range(requests_amount)]

    await asyncio.gather(*tasks)

asyncio.run(main())


