import asyncio

from activity import send_request
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import RequestWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="request-workflow-task-queue",
        workflows=[RequestWorkflow],
        activities=[send_request],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
