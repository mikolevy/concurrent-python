import threading

rabbits_colony_size: int = 0


def rabbit_counter(number_of_rabbits: int):
    global rabbits_colony_size
    rabbits_colony_size += number_of_rabbits
    print(f'Now we have {rabbits_colony_size} rabbits')
    print('---------------')


for _ in range(10):
    threading.Thread(target=rabbit_counter, args=[1]).start()

print('All rabbits are counted')
