from datetime import datetime
from dataclasses import dataclass
from decimal import Decimal

from src.domain.enums import RideStatus
from src.domain.value_objects import GeoPoint


@dataclass
class Ride:
    passenger_id: int
    pickup_address: str
    pickup_geo: GeoPoint
    destination_address: str
    destination_geo: GeoPoint
    status: RideStatus
    distance_meters: float
    price: Decimal
    currency: str

    id: int | None = None
    assigned_driver_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
