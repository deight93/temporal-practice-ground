from pydantic import BaseModel, Field


class InitResponse(BaseModel):
    status: str = Field(title="response 상태", description="SUCCESS / FAIL")
    message: str | None = Field(
        default=None, title="메시지", description="SUCCESS / FAIL"
    )


class BaseResponse(InitResponse):
    number: int = Field(title="return 값", description="return 값 int형")
