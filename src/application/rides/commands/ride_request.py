from dataclasses import dataclass

from movex_domain.value_objects.geo_point import GeoPoint


@dataclass(frozen=True)
class RideRequestCommand:
    pickup: GeoPoint
    destination: GeoPoint
    user_id: int
