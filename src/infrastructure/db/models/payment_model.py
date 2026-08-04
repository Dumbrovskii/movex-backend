from datetime import datetime

from src.infrastructure.db import Base
from src.domain.enums import PaymentStatus

from sqlalchemy import String, TIMESTAMP, BigInteger, Identity, func, ForeignKey, DECIMAL, Enum as SQLEnum, TEXT
from sqlalchemy.orm import Mapped, mapped_column

class PaymentModel(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    ride_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("rides.id"), nullable=False)
    amount: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(SQLEnum(PaymentStatus, name="payment_status"), nullable=False)
    transaction_id: Mapped[str] = mapped_column(TEXT, unique=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )