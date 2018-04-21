import threading

worker_lock = threading.Lock()


def do_some_work():
    with worker_lock:
        print('I have lock when I am writing it!')


workers = []
for _ in range(10):
    thread = threading.Thread(target=do_some_work)
    workers.append(thread)
    thread.start()

for worker in workers:
    worker.join()

print('All work is done - bye bye!')
