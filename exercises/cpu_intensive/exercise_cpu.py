import random

from exercises.utils import time_counter


def process_intensive_cpu_operations(task_size):

    results = []
    for number in range(task_size):
        results.append(random.random())


with time_counter():

    for task_number in range(10):
        process_intensive_cpu_operations(10_000_000)

    print('All work is done - bye bye!')
