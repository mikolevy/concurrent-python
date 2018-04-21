import threading
import queue

tasks_queue = queue.Queue()


def process_tasks_from_queue():

    while True:
        task_data: str = tasks_queue.get()
        do_some_work(task_data)
        tasks_queue.task_done()


def do_some_work(task_data: str):
    print(f'Doing task_data: {task_data}...')


for _ in range(3):
    thread = threading.Thread(target=process_tasks_from_queue, daemon=True)
    thread.start()


for task_number in range(10):
    tasks_queue.put(f'Task number: {task_number}')

tasks_queue.join()

print('All work is done - bye bye!')
