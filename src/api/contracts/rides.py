from decimal import Decimal

from pydantic import BaseModel, Field

from src.domain.value_objects import Route
from src.domain.entities.ride import Ride


class RideEstimateRequest(BaseModel):
    pickup_latitude: float = Field(ge=-90, le=90)
    pickup_longitude: float = Field(ge=-180, le=180)

    destination_latitude: float = Field(ge=-90, le=90)
    destination_longitude: float = Field(ge=-180, le=180)


class RideEstimateResponse(BaseModel):
    distance_meters: float
    duration_seconds: float
    geometry: list[list[float]]
    waypoints: list[list[float]]
    price: Decimal
    currency: str

class RideRequest(BaseModel):
    pickup_latitude: float = Field(ge=-90, le=90)
    pickup_longitude: float = Field(ge=-180, le=180)

    destination_latitude: float = Field(ge=-90, le=90)
    destination_longitude: float = Field(ge=-180, le=180)

class RideResponse(BaseModel):
    ride: Ride
    route: Route

class RideActiveResponse(BaseModel):
    route: Route
    ride: Ride

class RideCancelRequest(BaseModel):
    ride_id: int
