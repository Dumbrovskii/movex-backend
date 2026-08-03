from dataclasses import dataclass

@dataclass(frozen=True)
class GeoPoint:
    latitude: float
    longitude: float