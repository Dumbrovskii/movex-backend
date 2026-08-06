from abc import ABC, abstractmethod


class RefreshTokenRepository(ABC):

    @abstractmethod
    async def save(
            self,
            token: str,
            user_id: int,
            ttl_seconds: int,
    ) -> None:
        pass

    @abstractmethod
    async def get_user_id(
            self,
            token: str,
    ) -> int | None:
        pass

    @abstractmethod
    async def delete(
            self,
            token: str,
    ) -> None:
        pass