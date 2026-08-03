from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import DECIMAL
from src.domain.enums import PaymentStatus


@dataclass
class Payment:
    id: int
    ride_id: int
    amount: DECIMAL
    currency: str
    status: PaymentStatus
    transaction_id: str
    created_at: datetime
    updated_at: datetime
