import asyncio
import random

from exercises.utils import time_counter


async def fetch_url(url):
    print(f'Fetchning url: {url}...')
    await asyncio.sleep(3)
    return f'Data from: {url}'


async def fetch_some_urls():
    urls = [f'funny-url-{url_number}' for url_number in range(3)]

    fetch_tasks = [asyncio.ensure_future(fetch_url(url)) for url in urls]
    await asyncio.wait(fetch_tasks)


async def do_some_work():
    results = []
    print('Doing some hard work')
    for _ in range(10_000_000):
        results.append(random.random)

    print('Ufff - now will fetch one URL...')
    response = await fetch_url('HARD-WORK-URL')
    print(response)


with time_counter():
    event_loop = asyncio.get_event_loop()
    tasks = [event_loop.create_task(fetch_some_urls()), event_loop.create_task(do_some_work())]
    wait_tasks = asyncio.wait(tasks)
    event_loop.run_until_complete(wait_tasks)
    event_loop.close()

