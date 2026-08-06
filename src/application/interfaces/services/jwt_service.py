from abc import ABC, abstractmethod


class JwtService(ABC):

    @abstractmethod
    def create_access_token(
            self,
            user_id: int,
    ) -> str:
        pass

    @abstractmethod
    def decode_access_token(
            self,
            token: str,
    ) -> dict:
        pass