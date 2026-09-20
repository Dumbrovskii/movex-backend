from dataclasses import dataclass

from src.domain.value_objects import GeoPoint


@dataclass(frozen=True)
class RideEstimateCommand:
    pickup: GeoPoint
    destination: GeoPoint
