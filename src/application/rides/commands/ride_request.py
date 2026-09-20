from dataclasses import dataclass

from src.domain.value_objects import GeoPoint


@dataclass(frozen=True)
class RideRequestCommand:
    pickup: GeoPoint
    destination: GeoPoint
    user_id: int
