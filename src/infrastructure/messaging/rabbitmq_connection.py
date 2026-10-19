import aio_pika
from aio_pika.abc import (
    AbstractRobustChannel,
    AbstractRobustConnection,
    AbstractRobustExchange,
)
from aio_pika import ExchangeType

from src.config.settings import settings


class RabbitMQConnection:
    def __init__(self) -> None:
        self._connection: AbstractRobustConnection | None = None
        self._channel: AbstractRobustChannel | None = None
        self._exchange: AbstractRobustExchange | None = None

    async def connect(self) -> None:
        self._connection = await aio_pika.connect_robust(
            settings.RABBITMQ_URL,
        )

        self._channel = await self._connection.channel(
            publisher_confirms=True,
            on_return_raises=True,
        )

        self._exchange = await self._channel.declare_exchange(
            name=settings.RABBITMQ_EXCHANGE,
            type=ExchangeType.TOPIC,
            durable=True,
        )
    
    async def close(self) -> None:
        if self._connection is not None:
            await self._connection.close()
        
        self._connection = None
        self._channel = None
        self._exchange = None
    
    @property
    def exchange(self) -> AbstractRobustExchange:
        if self._exchange is None:
            raise RuntimeError(
                "RabbitMQ connection has not been initialized"
            )
        
        return self._exchange
