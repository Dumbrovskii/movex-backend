from fastapi import Depends

from src.application.auth.use_cases import (
    RequestCodeUseCase,
    VerifyCodeUseCase,
    RefreshTokenUseCase,
)
from src.application.interfaces import (
    SmsSender,
    TokenService,
    UserRepository,
    VerificationCodeRepository,
    RefreshTokenRepository,
)

from .providers import (
    get_token_service,
    get_user_repository,
    get_sms_sender,
    get_verification_code_repository,
    get_refresh_token_repository,
)


def get_request_code_use_case(
        verification_code_repository: VerificationCodeRepository = Depends(get_verification_code_repository),
        sms_sender: SmsSender = Depends(get_sms_sender),
) -> RequestCodeUseCase:
    return RequestCodeUseCase(
        repository=verification_code_repository,
        sms_sender=sms_sender,
    )

async def get_verify_code_use_case(
        verification_code_repository: VerificationCodeRepository = Depends(get_verification_code_repository),
        token_service: TokenService = Depends(get_token_service),
        user_repository: UserRepository = Depends(get_user_repository),
) -> VerifyCodeUseCase:

    return VerifyCodeUseCase(
        verification_code_repository=verification_code_repository,
        token_service=token_service,
        user_repository=user_repository,
    )

async def get_refresh_token_use_case(
        refresh_token_repository: RefreshTokenRepository = Depends(get_refresh_token_repository),
        token_service: TokenService = Depends(get_token_service)
) -> RefreshTokenUseCase:

    return RefreshTokenUseCase(
        refresh_token_repository=refresh_token_repository,
        token_service=token_service,
    )