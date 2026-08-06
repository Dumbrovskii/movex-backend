from secrets import randbelow

from src.config.settings import settings


def generate_verification_code() -> str:
    upper_bound = 10 ** settings.VERIFICATION_CODE_LENGTH

    return f"{randbelow(upper_bound):0{settings.VERIFICATION_CODE_LENGTH}d}"