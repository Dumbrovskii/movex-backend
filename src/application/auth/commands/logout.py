from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class LogoutCommand:
    refresh_token: str