from core.settings import EnvSettings
from fastapi import FastAPI, HTTPException
from schemas.schemas import BaseResponse
from services import services

settings = EnvSettings()
app = FastAPI()


@app.get("/")
async def root() -> BaseResponse:
    match settings.APP_NAME:
        case "server1":
            service = services.random_delay()
        case "server2":
            service = services.half_chance_failure()
        case "server3":
            service = services.get_four()
        case "server4":
            service = services.get_negative_twenty()
        case _:
            raise HTTPException(status_code=404, detail="env error!")

    return service
