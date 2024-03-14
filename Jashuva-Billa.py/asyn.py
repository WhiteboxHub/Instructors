import asyncio
import aiohttp


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
   
async def main():
    urls = [
        'https://www.example.com',
        'https://www.example.org',
        'https://www.example.net'
    ]

    tasks = [fetch_page(url) for url in urls]
    pages = await asyncio.gather(*tasks)


    for page in pages:
        print(page[:100])  

asyncio.run(main())




















import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  
    print(f"Goodbye, {name}!")

async def main():
    await greet("Jashuva")
    await greet("Billa")

asyncio.run(main())