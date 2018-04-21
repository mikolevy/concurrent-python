rabbits_colony_size: int = 0


def rabbit_counter(number_of_rabbits: int):
    global rabbits_colony_size
    rabbits_colony_size += number_of_rabbits
    print(f'Now we have {rabbits_colony_size} rabbits')
    print('---------------')


for _ in range(10):
    rabbit_counter(1)

print('All rabbits are counted')
