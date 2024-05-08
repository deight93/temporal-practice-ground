import asyncio
from datetime import timedelta

from temporalio.client import Client
from workflow import AsyncScenario, AsyncSyncScenario, SyncScenario


async def run_workflow():
    client = await Client.connect("localhost:7233")
    urls = [f"http://localhost:{port}" for port in range(8001, 8004)]

    # Scenario1 비동기 실행
    scenario1_future = client.start_workflow(
        AsyncScenario.run, urls, id="request-workflow-1", task_queue="request-tasks"
    )

    # Scenario2 동기 실행
    scenario2_future = client.start_workflow(
        SyncScenario.run, urls, id="request-workflow-2", task_queue="request-tasks"
    )

    # Scenario3 30초 후 비동기 실행
    urls = [f"http://localhost:{port}" for port in [8001, 8002, 8004]]
    scenario3_future = client.start_workflow(
        AsyncScenario.run,
        urls,
        id="request-workflow-3",
        task_queue="request-tasks",
        start_delay=timedelta(seconds=30),
    )

    # Scenario4 20초마다 비동기 실행
    urls = [f"http://localhost:{port}" for port in [8002, 8003, 8005]]
    scenario4_future = client.start_workflow(
        AsyncSyncScenario.run,
        urls,
        id="request-workflow-4",
        task_queue="request-tasks",
        cron_schedule="* * * * *",
    )

    # 워크플로우 실행 결과 얻기
    scenario1_result = await scenario1_future
    scenario2_result = await scenario2_future
    scenario3_result = await scenario3_future
    scenario4_result = await scenario4_future

    print(f"Scenario1 result: {scenario1_result}")
    print(f"Scenario2 result: {scenario2_result}")
    print(f"Scenario3 result: {scenario3_result}")
    print(f"Scenario4 result: {scenario4_result}")


if __name__ == "__main__":
    asyncio.run(run_workflow())
