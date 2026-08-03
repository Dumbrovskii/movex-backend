from dataclasses import dataclass
from datetime import datetime
from src.domain.enums import NotificationType


@dataclass
class Notification:
    id: int
    user_id: int
    type: NotificationType
    title: str
    message: str
    created_at: datetime
    read_at: datetime