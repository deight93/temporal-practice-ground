import secrets
import time

from fastapi import HTTPException


def random_delay():
    number = 10

    # Business Logic
    seconds = secrets.randbelow(5) + 3
    time.sleep(seconds)

    response = {"status": "SUCCESS", "number": number}
    return response


def half_chance_failure():
    number = 100

    # Business Logic
    if secrets.randbelow(2) == 0:
        raise HTTPException(status_code=400, detail="Fail!")
    response = {"status": "SUCCESS", "number": number}
    return response


def get_four():
    number = 4

    # Business Logic

    response = {"status": "SUCCESS", "number": number}
    return response


def get_negative_twenty():
    number = -20

    # Business Logic

    response = {"status": "SUCCESS", "number": number}
    return response
