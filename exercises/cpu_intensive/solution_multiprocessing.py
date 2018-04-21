import random
from multiprocessing.pool import Pool

from exercises.utils import time_counter


def process_intensive_cpu_operations(task_size):

    results = []
    for number in range(task_size):
        results.append(random.random())


if __name__ == '__main__':

    with time_counter():
        with Pool(processes=4) as workers_pool:
            tasks = [10_000_000 for _ in range(10)]
            workers_pool.map(process_intensive_cpu_operations, tasks)

        print('All work is done - bye bye!')
