from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class RefreshTokenCommand:
    refresh_token: str