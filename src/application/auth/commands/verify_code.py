from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class VerifyCodeCommand:
    phone: str
    code: str