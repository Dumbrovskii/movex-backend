from redis.asyncio import Redis

from src.config.settings import settings


redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB_NAME,
    decode_responses=True,
)