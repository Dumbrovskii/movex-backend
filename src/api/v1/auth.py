from fastapi import APIRouter, Depends

from src.api.contracts.auth import (
    RequestCodeRequest,
    RequestCodeResponse,
    VerifyCodeRequest,
    VerifyCodeResponse,
    RefreshTokenRequest,
    RefreshTokenResponse,
)
from src.application.auth.commands import (
    RequestCodeCommand,
    VerifyCodeCommand,
    RefreshTokenCommand,
)
from src.application.auth.use_cases import (
    RequestCodeUseCase,
    VerifyCodeUseCase,
    RefreshTokenUseCase,
)
from src.api.dependencies.auth import (
    get_request_code_use_case,
    get_verify_code_use_case,
    get_refresh_token_use_case,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/request-code",
    response_model=RequestCodeResponse,
)
async def request_code(
        request: RequestCodeRequest,
        use_case: RequestCodeUseCase = Depends(get_request_code_use_case),
):
    command = RequestCodeCommand(
        phone=request.phone
    )

    await use_case.execute(command)

    return RequestCodeResponse(
        success=True,
    )


@router.post(
    "/verify-code",
    response_model=VerifyCodeResponse,
)
async def verify_code(
        request: VerifyCodeRequest,
        use_case: VerifyCodeUseCase = Depends(get_verify_code_use_case),
):
    command = VerifyCodeCommand(
        phone=request.phone,
        code=request.code,
    )
    access_token, refresh_token = await use_case.execute(command)

    return VerifyCodeResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )

@router.post(
    "/refresh",
    response_model=RefreshTokenResponse,
)
async def refresh_token(
        request: RefreshTokenRequest,
        use_case: RefreshTokenUseCase = Depends(get_refresh_token_use_case),
):
    command = RefreshTokenCommand(
        refresh_token=request.refresh_token,
    )

    access_token, refresh_token = await use_case.execute(command)

    return RefreshTokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )