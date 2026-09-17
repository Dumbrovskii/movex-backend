import httpx
from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces import (
    JwtService,
    RefreshTokenService,
    SmsSender,
    RefreshTokenRepository,
    UserRepository,
    VerificationCodeRepository,
    TokenService,
)
from src.infrastructure.db.repositories import SqlAlchemyUserRepository
from src.infrastructure.db.session import get_session
from src.infrastructure.redis import (
    RedisVerificationCodeRepository,
    RedisRefreshTokenRepository,
    redis,
)
from src.infrastructure.security import (
    PyJwtService,
    DefaultRefreshTokenService,
    DefaultTokenService,
)

from src.infrastructure.sms import DummySmsSender


def get_verification_code_repository() -> VerificationCodeRepository:
    return RedisVerificationCodeRepository(redis)

def get_refresh_token_repository() -> RefreshTokenRepository:
    return RedisRefreshTokenRepository(redis)

async def get_user_repository( session: AsyncSession = Depends(get_session),) -> UserRepository:
    return SqlAlchemyUserRepository(session)

def get_sms_sender() -> SmsSender:
    return DummySmsSender()

def get_jwt_service() -> JwtService:
    return PyJwtService()

def get_refresh_token_service() -> RefreshTokenService:
    return DefaultRefreshTokenService()

def get_token_service(
        jwt_service: JwtService = Depends(get_jwt_service),
        refresh_token_service: RefreshTokenService = Depends(get_refresh_token_service),
        refresh_token_repository: RefreshTokenRepository = Depends(get_refresh_token_repository),
) -> TokenService:
    return DefaultTokenService(
        jwt_service=jwt_service,
        refresh_token_service=refresh_token_service,
        refresh_token_repository=refresh_token_repository,
    )

def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client