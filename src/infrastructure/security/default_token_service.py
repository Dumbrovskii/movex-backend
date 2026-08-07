from src.application.interfaces import (
    JwtService,
    RefreshTokenRepository,
    RefreshTokenService,
    TokenService
)
from src.config.settings import settings


class DefaultTokenService(TokenService):

    def __init__(
            self,
            jwt_service: JwtService,
            refresh_token_service: RefreshTokenService,
            refresh_token_repository: RefreshTokenRepository,
    ) -> None:
        self._jwt_service = jwt_service
        self._refresh_token_service = refresh_token_service
        self._refresh_token_repository = refresh_token_repository

    async def issue_tokens(
            self,
            user_id: int
    ) -> tuple[str, str]:

        access_token = self._jwt_service.create_access_token(user_id)

        refresh_token = self._refresh_token_service.generate()

        await self._refresh_token_repository.save(
            token=refresh_token,
            user_id=user_id,
            ttl_seconds=settings.REFRESH_TOKEN_TTL_DAYS * 24 * 60 * 60
        )

        return access_token, refresh_token