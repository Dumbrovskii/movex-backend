from src.infrastructure.db.models import UserModel
from src.domain.entities import User


class UserMapper:
    """Converts User <-> UserModel."""
    @staticmethod
    def to_domain(model: UserModel) -> User:
        if model is None:
            raise ValueError("UserModel cannot be None")

        return User(
            id=model.id,
            phone=model.phone,
            full_name=model.full_name,
            email=model.email,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )

    @staticmethod
    def to_model(domain: User) -> UserModel:
        if User is None:
            raise ValueError("User cannot be null")

        return UserModel(
            id=domain.id,
            phone=domain.phone,
            full_name=domain.full_name,
            email=domain.email,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            deleted_at=domain.deleted_at,
        )