from dataclasses import dataclass


@dataclass(frozen=True)
class UserUpdateCurrentCommand:
    user_id: int
    changes: dict[str, str | None]
