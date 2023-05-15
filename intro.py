# Threading and Asynchronus

import threading
import asyncio


def ThreadingExample():
    
    def parallel(x):
        while True:
            print(x)


    arguments = ('A','Mo','Quant','Has','Arrived')
    thread = {}

    for i, j in enumerate(arguments):
        thread[i] = threading.Thread(target=parallel, args=(j,))

    for i, j in thread.items():
        j.start()

    for i, j in thread.items():
        j.join()


def AsyncExample():

    async def watch(x, y):
        while True:
            print(x)
            await asyncio.sleep(y)

    async def main():
        arguments = ('Mo','is','a','good','programmer')
        timers = (5, 10, 1, 3, 2)

        tasks = [asyncio.ensure_future(watch(i, j)) for i, j in zip(arguments, timers)]
        await asyncio.wait(tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    
def Combined():

    arguments = ('Mo','is','a','good','programmer')
    timers = (5, 10, 1, 3, 2)

    async def main(tag, x, y):
        while True:
            for i, j in zip(x, y):
                print(tag, i)
                await asyncio.sleep(j)
            

    def Base(tag):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main(tag, arguments, timers))


    td = lambda fun, *args: threading.Thread(target=fun, args=args)

    t1 = td(Base, 'Mo')
    t2 = td(Base, 'Quant')
    t3 = td(Base, 'Programs')
    t4 = td(Base, 'Python')

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

Combined()


    
