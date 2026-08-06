from datetime import UTC, datetime, timedelta

import jwt

from src.application.interfaces import JwtService
from src.config import settings

class PyJwtService(JwtService):

    def create_access_token(
            self,
            user_id: int,
    ) -> str:
        now = datetime.now(UTC)

        payload = {
            "sub": str(user_id),
            "iat": now,
            "exp": now + timedelta(
                minutes=settings.ACCESS_TOKEN_TTL_MINUTES,
            ),
        }

        return jwt.encode(
            payload=payload,
            key=settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )

    def decode_access_token(
            self,
            token: str,
    ) -> dict:
        return jwt.decode(
            jwt=token,
            key=settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )