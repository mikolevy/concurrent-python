import threading

from exercises.utils import fuzzy

rabbits_colony_size: int = 0


def rabbit_counter(number_of_rabbits: int):
    global rabbits_colony_size
    fuzzy()
    rabbits_colony_size += number_of_rabbits
    fuzzy()
    print(f'Now we have {rabbits_colony_size} rabbits')
    fuzzy()
    print('---------------')
    fuzzy()


for _ in range(10):
    threading.Thread(target=rabbit_counter, args=[1]).start()
    fuzzy()

print('All rabbits are counted')
fuzzy()
