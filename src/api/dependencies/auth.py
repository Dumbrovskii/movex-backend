from src.application.auth import (
    RequestCodeUseCase,
    VerifyCodeUseCase
)
from src.infrastructure.redis import (
    RedisVerificationCodeRepository,
    RedisRefreshTokenRepository,
    redis,
)
from src.infrastructure.security import (
    PyJwtService,
    DefaultRefreshTokenService
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
    verification_code_repository = RedisVerificationCodeRepository(redis)
    refresh_token_repository = RedisRefreshTokenRepository(redis)
    jwt_service = PyJwtService()
    refresh_token_service = DefaultRefreshTokenService()

    return VerifyCodeUseCase(
        verification_code_repository=verification_code_repository,
        refresh_token_repository=refresh_token_repository,
        jwt_service=jwt_service,
        refresh_token_service=refresh_token_service,
    )