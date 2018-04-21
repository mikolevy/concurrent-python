import threading

from exercises.utils import fuzzy

rabbits_colony_size: int = 0

counter_lock = threading.Lock()
printer_lock = threading.Lock()


def rabbit_counter(number_of_rabbits: int):
    global rabbits_colony_size
    fuzzy()
    with counter_lock:
        fuzzy()
        rabbits_colony_size += number_of_rabbits
        fuzzy()
        with printer_lock:
            fuzzy()
            print(f'Now we have {rabbits_colony_size} rabbits')
            fuzzy()
            print('---------------')


workers = []
for _ in range(10):
    worker = threading.Thread(target=rabbit_counter, args=[1])
    workers.append(worker)
    worker.start()
    fuzzy()

for worker in workers:
    worker.join()

fuzzy()
print('All rabbits are counted')
