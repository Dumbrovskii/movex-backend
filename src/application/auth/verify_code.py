from dataclasses import dataclass

from src.application.exceptions import (
    VerificationCodeNotFoundError,
    InvalidVerificationCodeError,
)

from src.application.interfaces import VerificationCodeRepository


@dataclass(slots=True, frozen=True)
class VerifyCodeCommand:
    phone: str
    code: str


class VerifyCodeUseCase:

    def __init__(
            self,
            repository: VerificationCodeRepository,
    ) -> None:
        self._repository = repository

    async def execute(
            self,
            command: VerifyCodeCommand,
    ) -> tuple[str, str]:
        stored_code = await self._repository.get_code(
            command.phone,
        )

        if stored_code is None:
            raise VerificationCodeNotFoundError()

        if stored_code != command.code:
            raise InvalidVerificationCodeError()

        await self._repository.delete_code(
            command.phone,
        )

        access_token = "access-token"
        refresh_token = "refresh-token"

        return (
            access_token,
            refresh_token,
        )
