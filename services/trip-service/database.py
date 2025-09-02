from typing import Optional

from typing_extensions import TypedDict


class Coord(TypedDict):
    lat: float
    lng: float


class Trip(TypedDict):
    id: int
    status: str
    user: str
    rider: int
    destination: Coord
    location: Coord
    amount: float


trips: list[Trip] = []


class Database:
    @staticmethod
    def list():
        return trips

    @staticmethod
    def create(dto: Trip):
        trips.append(dto)
        return dto

    @staticmethod
    def update(dto: Trip) -> Optional[Trip]:
        for i, trip in enumerate(trips):
            if trip["id"] == dto["id"]:
                trips[i] = {**trip, **dto}
                return dto
        return None
