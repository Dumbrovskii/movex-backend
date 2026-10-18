from src.application.users.commands import UserGetCurrentCommand
from movex_domain.entities.user import User

from src.application.interfaces import (
    UserRepository,
)

class UserGetCurrentUseCase:

    def __init__(
            self,
            user_repository: UserRepository,
    ):
        self._user_repository = user_repository

    async def execute(
            self,
            command: UserGetCurrentCommand
    ) -> User | None:
        user = await self._user_repository.get_by_id(
            user_id=command.user_id,
        )

        return user
