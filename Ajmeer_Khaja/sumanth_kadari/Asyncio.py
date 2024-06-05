import asyncio

async def fn():
    print("this is")  #after this prints it waits 1 sec
    await asyncio.sleep(1)
    print("asyncchronous programming")
    await asyncio.sleep(1)
    print("and not multithreading")
    
asyncio.run(fn())  #this is the run function 

''' 
async def main():
   # task=asyncio.create_task()
    print("A")
    await func() #here wait until 2nd function will be done
    print("B")
    
async def func():
    print("1")
    await asyncio.sleep(2)
    print("2")
asyncio.run(main())'''


async def main():
    task=asyncio.create_task(func())  #here printg parelle two functions one by one
    print("A")
    await asyncio.sleep(1)
    print("B")
    
async def func():
    print("1")
    await asyncio.sleep(1)
    print("2")
    
asyncio.run(main())



    