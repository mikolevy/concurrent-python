import random
import threading
import queue

from exercises.utils import time_counter

tasks_queue = queue.Queue()


def process_intensive_cpu_operations():

    while True:
        task_size = tasks_queue.get()
        results = []
        for number in range(task_size):
            results.append(random.random())
        tasks_queue.task_done()


for _ in range(4):
    thread = threading.Thread(target=process_intensive_cpu_operations, daemon=True)
    thread.start()

with time_counter():
    for task_number in range(10):
        tasks_queue.put(10_000_000)

    tasks_queue.join()

    print('All work is done - bye bye!')
