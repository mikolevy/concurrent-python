import time

from exercises.utils import time_counter


def fetch_url_resource(url):
    time.sleep(2)


with time_counter():
    urls_to_fetch = [f'nice-url-{url_number}' for url_number in range(10)]

    for url in urls_to_fetch:
        fetch_url_resource(url)
