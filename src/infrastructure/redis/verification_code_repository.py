from redis.asyncio import Redis

from src.application.interfaces import VerificationCodeRepository


class RedisVerificationCodeRepository(VerificationCodeRepository):

    def __init__(
            self,
            redis: Redis,
    ) -> None:
        self._redis = redis

    async def save_code(
            self,
            phone: str,
            code: str,
            ttl_seconds: int,
    ) -> str | None:
        await self._redis.set(
            name=f"verification:{phone}",
            value=code,
            ex=ttl_seconds,
        )

    async def get_code(
            self,
            phone: str,
    ) -> str | None:
        value = await self._redis.get(
            name=f"verification:{phone}"
        )

        if value is None:
            return None

        return str(value)

    async def delete_code(
            self,
            phone: str
    ) -> str | None:
        await self._redis.delete(
            f"verification:{phone}",
        )

    async def can_request_code(
            self,
            phone: str,
    ) -> bool:
        exists = await self._redis.exists(
            f"verification:{phone}",
        )

        return exists == 0