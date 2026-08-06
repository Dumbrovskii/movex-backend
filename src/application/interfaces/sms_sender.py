from abc import ABC, abstractmethod


class SmsSender(ABC):

    @abstractmethod
    async def send(
            self,
            phone: str,
            messaga: str
    ) -> None:
        """Send SMS."""