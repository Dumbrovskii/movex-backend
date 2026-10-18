from fastapi import Depends

from src.application.users.use_cases import (
    UserGetCurrentUseCase,
    UserUpdateCurrentUseCase,
)
from src.application.interfaces import (
    UserRepository,
)
from .providers import (
    get_user_repository,
)


async def get_user_get_current_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserGetCurrentUseCase:
    return UserGetCurrentUseCase(
        user_repository=user_repository,
    )

async def get_user_update_use_case(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserUpdateCurrentUseCase:
    return UserUpdateCurrentUseCase(
        user_repository=user_repository,
    )
