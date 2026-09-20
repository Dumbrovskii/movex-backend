from decimal import Decimal

from pydantic import BaseModel, Field


class EstimateRideRequest(BaseModel):
    pickup_latitude: float = Field(ge=-90, le=90)
    pickup_longitude: float = Field(ge=-180, le=180)

    destination_latitude: float = Field(ge=-90, le=90)
    destination_longitude: float = Field(ge=-180, le=180)


class EstimateRideResponse(BaseModel):
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
    distance_meters: float
    duration_seconds: float
    geometry: list[list[float]]
    waypoints: list[list[float]]
    price: Decimal
    currency: str