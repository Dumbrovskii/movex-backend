from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    phone: str
    full_name: str
    email: str | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None