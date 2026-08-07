from src.application.auth.commands import LogoutCommand
from src.application.interfaces import RefreshTokenRepository


class LogoutUseCase:

    def __init__(
            self,
            refresh_token_repository: RefreshTokenRepository,
    ) -> None:
        self._refresh_token_repository = refresh_token_repository

    async def execute(
            self,
            command: LogoutCommand,
    ) -> None:
        await self._refresh_token_repository.delete(
            command.refresh_token,
        )