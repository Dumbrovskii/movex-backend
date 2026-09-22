from dataclasses import dataclass


@dataclass(frozen=True)
class RideActiveCommand:
    user_id: int
