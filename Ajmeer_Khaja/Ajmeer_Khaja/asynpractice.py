import asyncio

async def multipy(a,b):
    return a*b

async def main():
    print( await multipy(4,5))

# asyncio.run(main())


async def fun1():
    print('fun1 exictuion started')
    await asyncio.sleep(2)
    print('iam fun1')
    return 0
async def fun2():
    print('fun2 exicution started')
    await asyncio.sleep(4);
    print('fun2 exicuted')
    return 0
async def runfun():
    # await fun1()
    # await fun2()
    await asyncio.gather(
        fun1(),
        fun2()
    )

asyncio.run(runfun())
# runfun()
