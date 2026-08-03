from src.infrastructure.db.models import RatingModel
from src.domain.entities import Rating


class RatingMapper:
    """Converts Rating <-> RatingModel."""
    @staticmethod
    def to_domain(model: RatingModel) -> Rating:
        if model is None:
            raise ValueError("RatingModel cannot be None")

        return Rating(
            id=model.id,
            ride_id=model.ride_id,
            author_id=model.author_id,
            recipient_id=model.recipient_id,
            score=model.score,
            comment=model.comment,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(domain: Rating) -> RatingModel:
        if domain is None:
            raise ValueError("Rating cannot be None")

        return RatingModel(
            id=domain.id,
            ride_id=domain.ride_id,
            author_id=domain.author_id,
            recipient_id=domain.recipient_id,
            score=domain.score,
            comment=domain.comment,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )