import re

_PHONE_PATTERN = re.compile(r"^\+[1-9]\d{7,14}$")

def is_valid_phone_number(phone: str) -> bool:
    return bool(_PHONE_PATTERN.fullmatch(phone))