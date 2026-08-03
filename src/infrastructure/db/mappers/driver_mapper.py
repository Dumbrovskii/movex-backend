from src.infrastructure.db.models import DriverModel
from src.domain.entities import Driver


class DriverMapper:
    """Converts Driver <-> DriverModel."""
    @staticmethod
    def to_domain(model: DriverModel) -> Driver:
        if model is None:
            raise ValueError("DriverModel cannot be None")

        return Driver(
            user_id=model.user_id,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )

    @staticmethod
    def to_model(domain: Driver) -> DriverModel:
        if domain is None:
            raise ValueError("Driver cannot be None")

        return DriverModel(
            user_id=domain.user_id,
            status=domain.status,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            deleted_at=domain.deleted_at,
        )