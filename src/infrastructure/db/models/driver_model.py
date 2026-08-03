from datetime import datetime

from sqlalchemy import BigInteger, Enum as SQLEnum, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.enums import DriverStatus
from src.infrastructure.db import Base

class DriverModel(Base):
    __tablename__ = "drivers"

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), primary_key=True)
    status: Mapped[DriverStatus] = mapped_column(SQLEnum(DriverStatus, name="driver_status"), nullable=False)

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

    deleted_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )