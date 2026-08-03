from src.infrastructure.db.models import NotificationModel
from src.domain.entities.notification import Notification


class NotificationMapper:
    """Converts Notification <-> NotificationModel."""
    @staticmethod
    def to_domain(model: NotificationModel) -> Notification:
        if model is None:
            raise ValueError("NotificationModel cannot be None")

        return Notification(
            id=model.id,
            user_id=model.user_id,
            type=model.type,
            title=model.title,
            message=model.message,
            read_at=model.read_at,
            created_at=model.created_at,
        )

    @staticmethod
    def to_model(domain: Notification) -> NotificationModel:
        if domain is None:
            raise ValueError("Notification cannot be None")

        return NotificationModel(
            id=domain.id,
            user_id=domain.user_id,
            type=domain.type,
            title=domain.title,
            message=domain.message,
            created_at=domain.created_at,
            readed_at=domain.read_at,
        )
