from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point

from src.domain.value_objects import GeoPoint
from src.infrastructure.db.models import RideModel
from src.domain.entities import Ride


class RideMapper:
    """Converts Ride <-> RideModel."""
    @staticmethod
    def to_domain(model: RideModel) -> Ride:
        if model is None:
            raise ValueError("RideModel cannot be None")

        pickup_shape = to_shape(model.pickup_geo)
        destination_shape = to_shape(model.destination_geo)

        return Ride(
            id=model.id,
            passenger_id=model.passenger_id,
            assigned_driver_id=model.assigned_driver_id,
            pickup_address=model.pickup_address,
            pickup_geo=GeoPoint(
                longitude=pickup_shape.x,
                latitude=pickup_shape.y
            ),
            destination_address=model.destination_address,
            destination_geo=GeoPoint(
                longitude=destination_shape.x,
                latitude=destination_shape.y
            ),
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(domain: Ride) -> RideModel:
        if domain is None:
            raise ValueError("Ride cannot be None")

        return RideModel(
            id=domain.id,
            passenger_id=domain.passenger_id,
            assigned_driver_id=domain.assigned_driver_id,
            pickup_address=domain.pickup_address,
            pickup_geo=from_shape(
                Point(
                    domain.pickup_geo.longitude,
                    domain.pickup_geo.latitude
                ),
                srid=4326
            ),
            destination_address=domain.destination_address,
            destination_geo=from_shape(
                Point(
                    domain.destination_geo.longitude,
                    domain.destination_geo.latitude
                ),
                srid=4326
            ),
            status=domain.status,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )