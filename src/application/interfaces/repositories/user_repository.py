from abc import ABC, abstractmethod

from src.domain.entities import User

class UserRepository(ABC):

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