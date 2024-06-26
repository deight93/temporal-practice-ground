import asyncio
from datetime import timedelta
from typing import List

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activity import send_request


@workflow.defn
class AsyncScenario:
    @workflow.run
    async def run(self, urls: List[str]) -> int:
        """비동기적 실행 테스트

        Args:
            urls (List[str]): url 리스트

        Returns:
            int: 요청한 서버의 응답합
        """
        activity_futures = [
            workflow.execute_activity(
                send_request,
                url,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=RetryPolicy(
                    initial_interval=timedelta(seconds=5),
                    backoff_coefficient=1.5,
                    maximum_interval=timedelta(seconds=30),
                    maximum_attempts=5,
                ),
            )
            for url in urls
        ]
        results = await asyncio.gather(*activity_futures)
        return sum([result.get("number") for result in results])


@workflow.defn
class SyncScenario:
    @workflow.run
    async def run(self, urls: List[str]) -> int:
        """동기적 실행 테스트

        Args:
            urls (List[str]): url 리스트

        Returns:
            int: 요청한 서버의 응답합
        """
        results = []
        param = {}
        for url in urls:
            result = await workflow.execute_activity(
                send_request,
                args=[url, param],
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=RetryPolicy(
                    initial_interval=timedelta(seconds=5),
                    backoff_coefficient=1.5,
                    maximum_interval=timedelta(seconds=30),
                    maximum_attempts=5,
                ),
            )
            param["number"] = result.get("number")
            results.append(result)
        return sum([result.get("number") for result in results])


@workflow.defn
class AsyncSyncScenario:
    @workflow.run
    async def run(self, urls: List[str]) -> int:
        """시나리오5 동기, 비동기적 실행 테스트

        Args:
            urls (List[str]): url 리스트 [8002, 8003, 8005]

        Returns:
            int: 요청한 서버의 응답합
        """
        activity_futures = [
            workflow.execute_activity(
                send_request,
                url,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=RetryPolicy(
                    initial_interval=timedelta(seconds=5),
                    backoff_coefficient=1.5,
                    maximum_interval=timedelta(seconds=30),
                    maximum_attempts=5,
                ),
            )
            for url in urls[:-1]
        ]
        results = await asyncio.gather(*activity_futures)
        results_num = [result.get("number") for result in results]

        param = {"number1": results_num[0], "number2": results_num[1]}
        result = await workflow.execute_activity(
            send_request,
            args=[urls[-1], param],
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=RetryPolicy(
                initial_interval=timedelta(seconds=5),
                backoff_coefficient=1.5,
                maximum_interval=timedelta(seconds=30),
                maximum_attempts=5,
            ),
        )

        return result.get("number")
