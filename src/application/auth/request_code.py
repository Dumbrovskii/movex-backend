from dataclasses import dataclass

from src.application.exceptions import TooManyRequestsError
from src.application.interfaces import (
    SmsSender,
    VerificationCodeRepository,
)
from .code_generator import generate_verification_code
from src.config.settings import settings


@dataclass(slots=True, frozen=True)
class RequestCodeCommand:
    phone: str

class RequestCodeUseCase:

    def __init__(
            self,
            repository: VerificationCodeRepository,
            sms_sender: SmsSender,
    ) -> None:
        self._repository = repository
        self._sms_sender = sms_sender

    async def execute(
            self,
            command: RequestCodeCommand,
    ) -> None:
        can_request = await self._repository.can_request_code(
            command.phone,
        )

        if not can_request:
            raise TooManyRequestsError()

        code = generate_verification_code()

        await self._repository.save_code(
            phone=command.phone,
            code=code,
            ttl_seconds=settings.VERIFICATION_CODE_TTL_SECONDS,
        )

        await self._sms_sender.send(
            phone=command.phone,
            messaga=f"Your verification code is {code}",
        )