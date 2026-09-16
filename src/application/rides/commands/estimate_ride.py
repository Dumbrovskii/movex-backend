from dataclasses import dataclass

from src.domain.value_objects import GeoPoint


@dataclass(frozen=True)
class EstimateRideCommand:
    pickup: GeoPoint
    destination: GeoPoint
