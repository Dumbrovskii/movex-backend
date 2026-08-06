from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from src.application.exceptions import (
    TooManyRequestsError,
    InvalidVerificationCodeError,
    VerificationCodeNotFoundError,
)

def register_auth_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(TooManyRequestsError)
    async def too_many_requests_handler(
            request: Request,
            exc: TooManyRequestsError,
    ):
        return JSONResponse(
            status_code=429,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(VerificationCodeNotFoundError)
    async def verification_code_not_found_handler(
            request: Request,
            exc: VerificationCodeNotFoundError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc)
            }
        )

    @app.exception_handler(InvalidVerificationCodeError)
    async def invalid_verification_code_handler(
            request: Request,
            exc: InvalidVerificationCodeError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc)
            },
        )