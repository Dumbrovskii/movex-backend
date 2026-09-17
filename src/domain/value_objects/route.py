from dataclasses import dataclass
from src.domain.value_objects import GeoPoint


@dataclass(frozen=True)
class Route:
    distance_meters: float
    duration_seconds: float
    geometry: list[GeoPoint]
    waypoints: list[GeoPoint]