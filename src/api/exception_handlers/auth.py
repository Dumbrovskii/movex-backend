from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from src.application.exceptions import (
    InvalidPhoneNumberError,
    TooManyRequestsError,
    InvalidVerificationCodeError,
    VerificationCodeNotFoundError,
    InvalidRefreshTokenError,
    UnauthorizedError,
)

def register_auth_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(InvalidPhoneNumberError)
    async def invalid_phone_number_handler(
            request: Request,
            exc: InvalidPhoneNumberError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "error": {
                    "code": "INVALID_PHONE_NUMBER",
                    "message": str(exc),
                },
            },
        )

    @app.exception_handler(TooManyRequestsError)
    async def too_many_requests_handler(
            request: Request,
            exc: TooManyRequestsError,
    ):
        return JSONResponse(
            status_code=429,
            content={
                "error": {
                    "code": "TOO_MANY_REQUESTS",
                    "message": str(exc),
                },
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

    @app.exception_handler(InvalidRefreshTokenError)
    async def invalid_refresh_token_handler(
            request: Request,
            exc: InvalidRefreshTokenError
    ):
        return JSONResponse(
            status_code=401,
            content={
                "detail": str(exc)
            },
        )

    @app.exception_handler(UnauthorizedError)
    async def unauthorized_handler(
            request: Request,
            exc: UnauthorizedError,
    ):
        return JSONResponse(
            status_code=401,
            content={
                "error": {
                    "code": "UNAUTHORIZED",
                    "message": str(exc),
                },
            },
            headers={"WWW-Authenticate": "Bearer"}
        )