from abc import ABC, abstractmethod


class TokenService(ABC):

    @abstractmethod
    async def issue_tokens(
            self,
            user_id: int
    ) -> tuple[str, str]:
        pass