import aiohttp
from temporalio import activity


@activity.defn
async def send_request(url: str, params: dict | None = None) -> dict:
    if not params:
        params = {}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                raise aiohttp.ClientResponseError(
                    response.request_info,
                    response.history,
                    status=response.status,
                    message=f"Expected status code 200, but got {response.status}",
                )
            data = await response.json()
            return data
