from fastapi import Depends, FastAPI, HTTPException, Query

from app.core.settings import EnvSettings
from app.schemas.schemas import (
    BaseResponse,
    GetPlusRequest,
    PostAligoRequest,
    PostAligoResponse,
)
from app.services import services

settings = EnvSettings()
app = FastAPI()


match settings.APP_NAME:
    case "server1":

        @app.get("/", response_model=BaseResponse)
        async def root(number: int | None = Query(default=None)):
            service = services.random_delay(number)
            return service

    case "server2":

        @app.get("/", response_model=BaseResponse)
        async def root(number: int | None = Query(default=None)):
            service = services.half_chance_failure(number)
            return service

    case "server3":

        @app.get("/", response_model=BaseResponse)
        async def root(number: int | None = Query(default=None)):
            service = services.get_four(number)
            return service

    case "server4":

        @app.get("/", response_model=BaseResponse)
        async def root(number: int | None = Query(default=None)):
            service = services.get_negative_twenty(number)
            return service

    case "server5":

        @app.get("/", response_model=BaseResponse)
        async def root(
            param: GetPlusRequest = Depends(), number: int | None = Query(default=None)
        ):
            service = services.get_response_plus(param, number)
            return service

    case "server6":

        @app.post("/", response_model=PostAligoResponse)
        async def root(body: PostAligoRequest):
            service = services.post_aligo_test(body)
            return service

    case _:
        raise HTTPException(status_code=404, detail="env error!")
