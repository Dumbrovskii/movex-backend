from src.application.auth.commands import RequestCodeCommand

from src.application.exceptions import TooManyRequestsError
from src.application.interfaces import (
    SmsSender,
    VerificationCodeRepository,
)
from src.application.auth.code_generator import generate_verification_code
from src.config.settings import settings


class RequestCodeUseCase:

    def __init__(
            self,
            verification_code_repository: VerificationCodeRepository,
            sms_sender: SmsSender,
    ) -> None:
        self._verification_code_repository = verification_code_repository
        self._sms_sender = sms_sender

    async def execute(
            self,
            command: RequestCodeCommand,
    ) -> None:
        can_request = await self._verification_code_repository.can_request_code(
            command.phone,
        )

        if not can_request:
            raise TooManyRequestsError()

        code = generate_verification_code()

        await self._verification_code_repository.save_code(
            phone=command.phone,
            code=code,
            ttl_seconds=settings.VERIFICATION_CODE_TTL_SECONDS,
        )

        await self._sms_sender.send(
            phone=command.phone,
            messaga=f"Your verification code is {code}",
        )