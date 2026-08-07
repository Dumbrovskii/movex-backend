from src.application.exceptions import InvalidRefreshTokenError
from src.application.interfaces import (
    RefreshTokenRepository,
    TokenService,
)

from src.application.auth.commands import RefreshTokenCommand


class RefreshTokenUseCase:

    def __init__(
            self,
            refresh_token_repository: RefreshTokenRepository,
            token_service: TokenService,
    ) -> None:
        self._refresh_token_repository = refresh_token_repository
        self._token_service = token_service

    async def execute(
            self,
            command: RefreshTokenCommand,
    ) -> tuple[str, str]:

        user_id = await self._refresh_token_repository.get_user_id(
            command.refresh_token,
        )

        if user_id is None:
            raise InvalidRefreshTokenError()

        await self._refresh_token_repository.delete(
            command.refresh_token,
        )

        return await self._token_service.issue_tokens(user_id)