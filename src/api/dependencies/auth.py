from src.application.auth import (
    RequestCodeUseCase,
    VerifyCodeUseCase
)
from src.infrastructure.redis import (
    RedisVerificationCodeRepository,
    redis,
)
from src.infrastructure.sms import DummySmsSender


def get_request_code_use_case() -> RequestCodeUseCase:
    repository = RedisVerificationCodeRepository(redis)
    sms_sender = DummySmsSender()

    return RequestCodeUseCase(
        repository=repository,
        sms_sender=sms_sender,
    )

def get_verify_code_use_case() -> VerifyCodeUseCase:
    repository = RedisVerificationCodeRepository(redis)

    return VerifyCodeUseCase(
        repository=repository,
    )