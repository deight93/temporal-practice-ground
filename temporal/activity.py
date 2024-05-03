import aiohttp
from temporalio import activity


@activity.defn
async def send_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
