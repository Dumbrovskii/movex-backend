from dataclasses import dataclass

from src.application.exceptions import (
    VerificationCodeNotFoundError,
    InvalidVerificationCodeError,
)

from src.application.interfaces import (
    VerificationCodeRepository,
    RefreshTokenRepository,
    JwtService,
    RefreshTokenService,
)
from src.config import settings


@dataclass(slots=True, frozen=True)
class VerifyCodeCommand:
    phone: str
    code: str


class VerifyCodeUseCase:

    def __init__(
            self,
            verification_code_repository: VerificationCodeRepository,
            refresh_token_repository: RefreshTokenRepository,
            jwt_service: JwtService,
            refresh_token_service: RefreshTokenService
    ) -> None:
        self._verification_code_repository = verification_code_repository
        self._refresh_token_repository = refresh_token_repository
        self._jwt_service = jwt_service
        self._refresh_token_service = refresh_token_service

    async def execute(
            self,
            command: VerifyCodeCommand,
    ) -> tuple[str, str]:
        stored_code = await self._verification_code_repository.get_code(
            command.phone,
        )

        if stored_code is None:
            raise VerificationCodeNotFoundError()

        if stored_code != command.code:
            raise InvalidVerificationCodeError()

        user_id = 1

        access_token = self._jwt_service.create_access_token(
            user_id=user_id,
        )

        refresh_token = self._refresh_token_service.generate()

        await self._refresh_token_repository.save(
            token=refresh_token,
            user_id=user_id,
            ttl_seconds=settings.REFRESH_TOKEN_TTL_DAYS * 24 * 60 * 60,
        )

        await self._verification_code_repository.delete_code(
            command.phone,
        )

        return (
            access_token,
            refresh_token,
        )
