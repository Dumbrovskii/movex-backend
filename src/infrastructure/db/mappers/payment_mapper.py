from src.infrastructure.db.models import PaymentModel
from src.domain.entities import Payment


class PaymentMapper:
    """Converts Payment <-> PaymentModel."""
    @staticmethod
    def to_domain(model: PaymentModel) -> Payment:
        if model is None:
            raise ValueError("PaymentModel cannot be None")

        return Payment(
            id=model.id,
            ride_id=model.ride_id,
            amount=model.amount,
            currency=model.currency,
            status=model.status,
            transaction_id=model.transaction_id,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def to_model(domain: Payment) -> PaymentModel:
        if domain is None:
            raise ValueError("Payment cannot be None")

        return PaymentModel(
            id=domain.id,
            ride_id=domain.ride_id,
            amount=domain.amount,
            currency=domain.currency,
            status=domain.status,
            transaction_id=domain.transaction_id,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )