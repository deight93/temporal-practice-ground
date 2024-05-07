import asyncio

from activity import send_request
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import AsyncScenario, SyncScenario


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="request-tasks",
        workflows=[AsyncScenario, SyncScenario],
        activities=[send_request],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
