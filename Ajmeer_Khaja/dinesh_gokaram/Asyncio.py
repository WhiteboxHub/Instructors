import asyncio

async def say_hello(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    task1 = asyncio.create_task(say_hello(2, "Alice"))
    task2 = asyncio.create_task(say_hello(1, "Bob"))

    await asyncio.gather(task1, task2)

asyncio.run(main())

#----------Timeout Handling
import asyncio

async def time_consuming_task():
    await asyncio.sleep(5)
    print("Task completed successfully!")

async def main():
    try:
        await asyncio.wait_for(time_consuming_task(), timeout=3)
    except asyncio.TimeoutError:
        print("Task timed out.")

asyncio.run(main())

#----------Periodic Task:

import asyncio
from datetime import datetime

async def periodic_task():
    while True:
        print(f"Current time: {datetime.now()}")
        await asyncio.sleep(5)
asyncio.run(periodic_task())

#-----
import asyncio

async def long_running_task():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task cancelled.")

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(5)  # Run for 5 seconds
    task.cancel()
    await task

asyncio.run(main())
