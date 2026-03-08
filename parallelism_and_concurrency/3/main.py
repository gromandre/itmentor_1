import requests
import threading
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

def get_status_code(url):
    r = requests.get(url=url)
    with lock:
        with open("status_code.txt", "a") as f:
            f.write(f'{url[8:].replace("/", "")}: {r.status_code}\n')

def main():
    URL = 'https://example.com/'
    requests_amount = 50
    requests_limit = 10

    with ThreadPoolExecutor(max_workers=requests_limit) as pool:
        pool.map(get_status_code, [URL] * requests_amount)

if __name__ == "__main__":
    main()



