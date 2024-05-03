import asyncio

from temporalio.client import Client
from workflow import RequestWorkflow


async def run_workflow():
    client = await Client.connect("localhost:7233")
    urls = [f"http://localhost:{port}" for port in range(8001, 8005)]
    result = await client.execute_workflow(
        RequestWorkflow.run, urls, id="request-workflow", task_queue="request-tasks"
    )
    print(f"Workflow result: {result}")


if __name__ == "__main__":
    asyncio.run(run_workflow())
