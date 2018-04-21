import random
import time

from exercises.utils import time_counter


def fetch_url(url):
    print(f'Fetchning url: {url}...')
    time.sleep(3)
    return f'Data from: {url}'


def fetch_some_urls():
    urls = [f'funny-url-{url_number}' for url_number in range(3)]

    for url in urls:
        response = fetch_url(url)
        print(response)


def do_some_work():
    results = []
    print('Doing some hard work')
    for _ in range(10_000_000):
        results.append(random.random)

    print('Ufff - now will fetch one URL...')
    response = fetch_url('HARD-WORK-URL')
    print(response)


with time_counter():

    fetch_some_urls()
    do_some_work()
