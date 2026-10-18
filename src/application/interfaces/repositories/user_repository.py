from abc import ABC, abstractmethod

from movex_domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    async def get_by_id(
            self,
            user_id: int,
    ) -> User | None:
        pass

    @abstractmethod
    async def get_by_phone(
            self,
            phone: str,
    ) -> User | None:
        pass

    @abstractmethod
    async def create(
            self,
            phone: str,
    ) -> User:
        pass

    @abstractmethod
    async def get_or_create(
            self,
            phone: str,
    ) -> User:
        pass

    @abstractmethod
    async def update(
            self,
            user_id: int,
            changes: dict[str, str | None],
    ) -> User:
        pass
