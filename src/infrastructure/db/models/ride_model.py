from datetime import datetime
from decimal import Decimal

from src.infrastructure.db import Base
from src.domain.enums import RideStatus

from sqlalchemy import BigInteger, Identity, ForeignKey, TEXT, Enum as SQLEnum, TIMESTAMP, func, DOUBLE_PRECISION, DECIMAL, String
from sqlalchemy.orm import Mapped, mapped_column

from geoalchemy2 import Geography
from geoalchemy2.elements import WKBElement

class RideModel(Base):
    __tablename__ = "rides"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    passenger_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    assigned_driver_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("drivers.user_id"), nullable=True)
    pickup_address: Mapped[str] = mapped_column(TEXT, nullable=False)
    pickup_geo: Mapped[WKBElement] = mapped_column(Geography("POINT", srid=4326), nullable=False)
    destination_address: Mapped[str] = mapped_column(TEXT, nullable=False)
    destination_geo: Mapped[WKBElement] = mapped_column(Geography("POINT", srid=4326), nullable=False)
    status: Mapped[RideStatus] = mapped_column(SQLEnum(RideStatus, name="ride_status"), nullable=False)
    distance_meters: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)

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
