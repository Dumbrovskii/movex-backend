from datetime import datetime

from src.infrastructure.db import Base

from sqlalchemy import BigInteger, Identity, ForeignKey, SmallInteger, CheckConstraint, TEXT, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

class RatingModel(Base):
    __tablename__ = "ratings"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    ride_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("rides.id"), nullable=False)
    author_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    recipient_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)

    score: Mapped[int] = mapped_column(
        SmallInteger,
        CheckConstraint("score >= 0 AND rating <= 5", name="chk_score_range"),
        nullable=False,
    )

    comment: Mapped[str] = mapped_column(TEXT, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now,
        nullable=False,
    )