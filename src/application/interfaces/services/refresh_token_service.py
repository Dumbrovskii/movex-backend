from abc import ABC, abstractmethod


class RefreshTokenService(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass