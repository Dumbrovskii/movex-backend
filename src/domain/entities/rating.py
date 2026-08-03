from dataclasses import dataclass
from datetime import datetime


@dataclass
class Rating:
    id: int
    ride_id: int
    author_id: int
    recipient_id: int
    score: int
    comment: str
    created_at: datetime
    updated_at: datetime