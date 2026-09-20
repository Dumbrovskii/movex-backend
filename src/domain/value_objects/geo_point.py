from dataclasses import dataclass

@dataclass(frozen=True)
class GeoPoint:
    latitude: float
    longitude: float

    def to_wkt(self) -> str:
        return f"POINT({self.longitude} {self.latitude})"
