from src.application.interfaces import SmsSender


class DummySmsSender(SmsSender):

    async def send(
            self,
            phone: str,
            messaga: str
    ) -> None:
        print(f"SMS -> {phone}: {messaga}")