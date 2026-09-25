from dataclasses import dataclass

@dataclass(frozen=True)
class RideCancelCommand:
    user_id: int
    ride_id: int
