from src.application.users.commands import UserUpdateCurrentCommand
from src.application.auth.validators import is_valid_phone_number
from movex_domain.entities.user import User
from src.application.exceptions import (
    InvalidPhoneNumberError,
)
from src.application.interfaces import (
    UserRepository,
)

class UserUpdateCurrentUseCase:

    def __init__(
            self,
            user_repository: UserRepository,
    ):
        self._user_repository = user_repository

    async def execute(
            self,
            command: UserUpdateCurrentCommand
    ) -> User:
        if "phone" in command.changes:
            if not is_valid_phone_number(command.changes["phone"]):
                raise InvalidPhoneNumberError()

        user = await self._user_repository.update(
            user_id=command.user_id,
            changes=command.changes,
        )

        return user
