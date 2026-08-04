from datetime import datetime

from src.infrastructure.db import Base
from src.domain.enums import NotificationType

from sqlalchemy import BigInteger, Identity, ForeignKey, Enum as SQLEnum, TEXT, TIMESTAMP, func
from sqlalchemy.orm import mapped_column, Mapped

class NotificationModel(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    type: Mapped[NotificationType] = mapped_column(SQLEnum(NotificationType, name="notification_type"), nullable=False)
    title: Mapped[str] = mapped_column(TEXT, nullable=False)
    message: Mapped[str] = mapped_column(TEXT, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    read_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )