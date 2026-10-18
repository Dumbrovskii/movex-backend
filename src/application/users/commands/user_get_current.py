from dataclasses import dataclass


@dataclass(frozen=True)
class UserGetCurrentCommand:
    user_id: int
