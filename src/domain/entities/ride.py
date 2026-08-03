from datetime import datetime
from dataclasses import dataclass
from src.domain.enums import RideStatus
from src.domain.value_objects import GeoPoint


@dataclass
class Ride:
    id: int
    passenger_id: int
    assigned_driver_id: int | None
    pickup_address: str
    pickup_geo: GeoPoint
    destination_address: str
    destination_geo: GeoPoint
    status: RideStatus
    created_at: datetime
    updated_at: datetime