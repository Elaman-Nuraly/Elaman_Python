import aiohttp
import asyncio

async def fetch_json(session, url):

    async with session.get(url) as response:
        return await response.json()

async def main():

    async with aiohttp.ClientSession() as session:
        url = 'https://jsonplaceholder.typicode.com/posts'
        json_data = await fetch_json(session, url)
        return json_data

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    json_data = loop.run_until_complete(main())

    print(json_data)
    