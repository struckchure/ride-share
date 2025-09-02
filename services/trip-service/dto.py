import pydantic
from database import Coord


class RequestTripDto(pydantic.BaseModel):
    destination: Coord
    location: Coord
