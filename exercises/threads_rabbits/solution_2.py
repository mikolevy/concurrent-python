import queue
import threading

from exercises.utils import fuzzy

rabbits_colony_size: int = 0
counter_queue = queue.Queue()
printer_queue = queue.Queue()


def counter_worker():
    global rabbits_colony_size

    while True:
        number_of_rabbits: int = counter_queue.get()
        fuzzy()
        rabbits_colony_size += number_of_rabbits
        fuzzy()
        printer_queue.put(f'Now we have {rabbits_colony_size} rabbits')
        fuzzy()
        printer_queue.put('---------------')
        fuzzy()
        counter_queue.task_done()


def printer_worker():
    while True:
        fuzzy()
        data: str = printer_queue.get()
        fuzzy()
        print(data)
        fuzzy()
        printer_queue.task_done()


def rabbit_counter(number_of_rabbits: int):
    fuzzy()
    counter_queue.put(number_of_rabbits)


counter = threading.Thread(target=counter_worker, daemon=True)
printer = threading.Thread(target=printer_worker, daemon=True)
workers = []

counter.start()
printer.start()

for _ in range(10):
    worker_thread = threading.Thread(target=rabbit_counter, args=[1])
    workers.append(worker_thread)
    worker_thread.start()
    fuzzy()


for worker in workers:
    fuzzy()
    worker.join()

counter_queue.join()
fuzzy()
printer_queue.put('All rabbits are counted')
fuzzy()
printer_queue.join()


