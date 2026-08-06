from abc import ABC, abstractmethod


class VerificationCodeRepository(ABC):

    @abstractmethod
    async def save_code(
            self,
            phone: str,
            code: str,
            ttl_seconds: int,
    ) -> str | None:
        """Save verification code."""

    @abstractmethod
    async def get_code(
            self,
            phone: str,
    ) -> str | None:
        """Return verification code."""

    @abstractmethod
    async def delete_code(
            self,
            phone: str
    ) -> str | None:
        """Delete verification code."""

    @abstractmethod
    async def can_request_code(
            self,
            phone: str,
    ) -> bool:
        """Return True if a new verification code can be requested."""