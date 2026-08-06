from redis.asyncio import Redis

from src.application.interfaces import RefreshTokenRepository


class RedisRefreshTokenRepository(RefreshTokenRepository):

    def __init__(
            self,
            redis: Redis,
    ) -> None:
        self._redis = redis

    async def save(
            self,
            token: str,
            user_id: int,
            ttl_seconds: int,
    ) -> None:
        await self._redis.set(
            name=f"refresh:{token}",
            value=user_id,
            ex=ttl_seconds,
        )

    async def get_user_id(
            self,
            token: str,
    ) -> int | None:
        value = await self._redis.get(
            name=f"refresh:{token}",
        )

        if value is None:
            return None

        return int(value)

    async def delete(
            self,
            token: str,
    ) -> None:
        await self._redis.delete(
            f"refresh:{token}",
        )