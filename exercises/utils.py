import random
import time
from contextlib import contextmanager


def fuzzy():
    time.sleep(random.random())


@contextmanager
def time_counter():
    start_time = time.time()
    yield
    print(f"--- {time.time() - start_time} seconds --- ")
