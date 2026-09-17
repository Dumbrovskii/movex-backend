import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.application.exceptions import UnauthorizedError
from src.application.interfaces import JwtService
from src.api.dependencies.providers import get_jwt_service

bearer_scheme = HTTPBearer(auto_error=False)

async def get_current_user_id(
        authorization: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
        jwt_service: JwtService = Depends(get_jwt_service)
) -> int:

    if authorization is None:
        raise UnauthorizedError()

    token: str = authorization.credentials

    try:
        payload = jwt_service.decode_access_token(token)
    except jwt.PyJWTError:
        raise UnauthorizedError()

    subject = payload.get("sub")
    if not isinstance(subject, str):
        raise UnauthorizedError()

    try:
        return int(subject)
    except ValueError:
        raise UnauthorizedError()
