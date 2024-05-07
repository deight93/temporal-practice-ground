import secrets
import time

from fastapi import HTTPException

from app.schemas.schemas import (
    BaseResponse,
    GetPlusRequest,
    PostAligoRequest,
    PostAligoResponse,
)


def random_delay() -> BaseResponse:
    number = 10

    # Business Logic
    seconds = secrets.randbelow(5) + 3
    time.sleep(seconds)

    response = {"status": "SUCCESS", "number": number}
    return response


def half_chance_failure() -> BaseResponse:
    number = 100

    # Business Logic
    if secrets.randbelow(2) == 0:
        raise HTTPException(status_code=400, detail="Fail!")
    response = {"status": "SUCCESS", "number": number}
    return response


def get_four() -> BaseResponse:
    number = 4

    # Business Logic

    response = {"status": "SUCCESS", "number": number}
    return response


def get_negative_twenty() -> BaseResponse:
    number = -20

    # Business Logic

    response = {"status": "SUCCESS", "number": number}
    return response


def get_response_plus(param: GetPlusRequest) -> BaseResponse:
    number = -35

    # Business Logic
    number += param.number1 + param.number2

    response = {"status": "SUCCESS", "number": number}
    return response


def post_aligo_test(body: PostAligoRequest) -> PostAligoResponse:
    apikey = body.apikey
    response = {"code": 0, "status": "SUCCESS", "message": "SUCCESS"}
    if apikey != "KDH1234":
        response = {"code": -1, "status": "FAIL", "message": "INVALID_APIKEY"}

    # Business Logic
    if secrets.randbelow(2) == 0:
        response = {"code": -99, "status": "FAIL", "message": "FAIL"}
    return response
