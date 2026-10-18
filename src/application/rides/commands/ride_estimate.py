from dataclasses import dataclass

from movex_domain.value_objects.geo_point import GeoPoint


@dataclass(frozen=True)
class RideEstimateCommand:
    pickup: GeoPoint
    destination: GeoPoint
