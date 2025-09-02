import logging
from math import sqrt

from database import Coord, Database, trips
from dto import RequestTripDto
from fastapi import APIRouter, Header
from httpx import request
from typing_extensions import Annotated

logger = logging.getLogger("uvicorn.error")
logger.name = "Root Router"

root_router = APIRouter()


def dist_between_2_points(p1: Coord, p2: Coord):
    lat1, lng1 = p1["lat"], p1["lng"]
    lat2, lng2 = p2["lat"], p2["lng"]

    return sqrt((lat2 - lat1) ** 2 + (lng2 - lng1) ** 2)


PRICE_PER_KM = 100


@root_router.post("/trip")
def request_trip(
    dto: RequestTripDto,
    user: Annotated[str, Header(alias="x-user")],
):
    amount = PRICE_PER_KM * dist_between_2_points(dto.location, dto.destination)

    trip = Database.create(
        {
            "id": len(trips) + 1,
            "status": "Idle",
            "user": user,
            "amount": amount,
            **dto.model_dump(),
        }
    )

    trxn = request(
        "POST",
        "http://localhost:8082/transactions/payment",
        headers={"x-user": user},
        data={"amount": amount, "trip": trip["id"]},
    )
    logger.info(f"trxn req status: {trxn.status_code}")

    return trip


@root_router.get("/trip")
def list_trip(user: Annotated[str, Header(alias="x-user")]):
    return list(filter(lambda x: x["user"] == user, trips))
