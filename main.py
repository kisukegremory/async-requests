import requests
import time
import asyncio
import httpx


def sync():
    start_time = time.time()

    urls = [f'https://pokeapi.co/api/v2/pokemon/{n}' for n in range(1, 30)]
    reqs = [requests.get(url) for url in urls]

    print("--- %s seconds ---" % (time.time() - start_time))
    return reqs

async def req_async():
    start_time = time.time()

    async with httpx.AsyncClient() as client:

        urls = [f'https://pokeapi.co/api/v2/pokemon/{n}' for n in range(1, 30)]
        tasks = [client.get(url) for url in urls]
        reqs = await asyncio.gather(*tasks)
        

    print("--- %s seconds ---" % (time.time() - start_time))
    return reqs


if __name__ == '__main__':
    req1 = asyncio.run(req_async())
    req2 = sync()