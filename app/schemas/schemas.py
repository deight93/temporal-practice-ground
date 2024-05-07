from pydantic import BaseModel, Field


class InitResponse(BaseModel):
    status: str = Field(title="response 상태", description="SUCCESS / FAIL")
    message: str | None = Field(
        default=None, title="메시지", description="SUCCESS / FAIL"
    )


class BaseResponse(InitResponse):
    number: int = Field(title="return 값", description="return 값 int형")


class GetPlusRequest(BaseModel):
    number1: int = Field(title="server return 값", description="return 값 int형")
    number2: int = Field(title="server return 값", description="return 값 int형")


class PostAligoResponse(InitResponse):
    code: int = Field(title="code", description="0미만 에러")
    info: dict | None = Field(default=None, title="info", description="info")


class PostAligoRequest(BaseModel):
    apikey: str = Field(title="인증용 API Key", description="인증용 API Key")
    userid: str = Field(title="사용자id", description="사용자id")
    senderkey: str = Field(title="발신프로파일 키", description="발신프로파일 키")
    tpl_code: str = Field(title="템플릿 코드", description="템플릿 코드")
