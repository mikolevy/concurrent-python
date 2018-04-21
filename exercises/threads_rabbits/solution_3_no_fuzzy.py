import threading

rabbits_colony_size: int = 0

counter_lock = threading.Lock()
printer_lock = threading.Lock()


def rabbit_counter(number_of_rabbits: int):
    global rabbits_colony_size
    with counter_lock:
        rabbits_colony_size += number_of_rabbits
        with printer_lock:
            print(f'Now we have {rabbits_colony_size} rabbits')
            print('---------------')


workers = []
for _ in range(10):
    worker = threading.Thread(target=rabbit_counter, args=[1])
    workers.append(worker)
    worker.start()

for worker in workers:
    worker.join()

print('All rabbits are counted')
