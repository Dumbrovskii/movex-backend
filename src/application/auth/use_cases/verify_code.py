from src.application.auth.commands import VerifyCodeCommand
from src.domain.entities import User

from src.application.exceptions import (
    VerificationCodeNotFoundError,
    InvalidVerificationCodeError,
)

from src.application.interfaces import (
    VerificationCodeRepository,
    TokenService,
    UserRepository,
)


class VerifyCodeUseCase:

    def __init__(
            self,
            verification_code_repository: VerificationCodeRepository,
            token_service: TokenService,
            user_repository: UserRepository,
    ) -> None:
        self._verification_code_repository = verification_code_repository
        self._token_service = token_service
        self._user_repository = user_repository

    async def execute(
            self,
            command: VerifyCodeCommand,
    ) -> tuple[str, str, User]:
        stored_code = await self._verification_code_repository.get_code(
            command.phone,
        )

        if stored_code is None:
            raise VerificationCodeNotFoundError()

        if stored_code != command.code:
            raise InvalidVerificationCodeError()

        user = await self._user_repository.get_or_create(
            phone=command.phone,
        )

        await self._verification_code_repository.delete_code(
            command.phone,
        )

        access_token, refresh_token = await self._token_service.issue_tokens(
            user_id=user.id,
        )

        return access_token, refresh_token, user