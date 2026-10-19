import json
from typing import Any

import aio_pika
from aio_pika import DeliveryMode, ExchangeType, Message

from src.application.interfaces.messaging import MessagePublisher


class RabbitMQPublisher(MessagePublisher):

    def __init__(
        self,
        exchange: aio_pika.abc.AbstractExchange,
    ):
        self._exchange = exchange

    async def publish(
        self,
        routing_key: str,
        message: dict[str, Any],
    ) -> None:
        body = json.dumps(
            message,
            ensure_ascii=False,
        ).encode("utf-8")

        await self._exchange.publish(
            Message(
                body=body,
                content_type="application/json",
                delivery_mode=DeliveryMode.PERSISTENT,
            ),
            routing_key=routing_key,
            mandatory=True,
        )
