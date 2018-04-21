import queue
import threading
import time

from exercises.utils import time_counter

tasks_queue = queue.Queue()


def fetch_url_resource(url):
    time.sleep(2)


def process_io_operations():

    while True:
        url = tasks_queue.get()
        fetch_url_resource(url)
        tasks_queue.task_done()


with time_counter():
    urls_to_fetch = [f'nice-url-{url_number}' for url_number in range(10)]

    for _ in range(10):
        thread = threading.Thread(target=process_io_operations, daemon=True)
        thread.start()

    for url in urls_to_fetch:
        tasks_queue.put(url)

    tasks_queue.join()

    print('All work is done - bye bye!')
