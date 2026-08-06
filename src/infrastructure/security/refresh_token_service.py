from secrets import token_urlsafe

from src.application.interfaces import RefreshTokenService


class DefaultRefreshTokenService(RefreshTokenService):

    def generate(self) -> str:
        return token_urlsafe(64)