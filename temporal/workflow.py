from datetime import timedelta
from typing import List

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activity import send_request


@workflow.defn
class RequestWorkflow:
    @workflow.run
    async def run(self, urls: List[str]) -> List[str]:
        results = []
        for url in urls:
            result = await workflow.execute_activity(
                send_request,
                url,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=RetryPolicy(
                    initial_interval=timedelta(seconds=1),
                    backoff_coefficient=2.0,
                    maximum_interval=timedelta(seconds=10),
                    maximum_attempts=5,
                ),
            )
            results.append(result)
        return results
