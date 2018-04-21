import asyncio


async def rabbit_breeder():
    print('Rabbit breeder is WORKING')
    await asyncio.sleep(2)
    print('Rabbit breeder report: DONE')


async def snake_breeder():
    print('Snake breeder is WORKING')
    await asyncio.sleep(2)
    print('Snake breeder report: DONE')


async def farmer():
    print('They are waiting for their animals, so I will do some work...')
    await asyncio.sleep(1)
    print('Farmer: DONE!')


event_loop = asyncio.get_event_loop()
tasks = [
    event_loop.create_task(rabbit_breeder()),
    event_loop.create_task(snake_breeder()),
    event_loop.create_task(farmer())
]
event_loop.run_until_complete(asyncio.wait(tasks))
event_loop.close()
