from fastapi import Depends, Response
from src.api.routing import ProtectedAPIRouter

from src.api.contracts import (
    UserMeResponse,
    UserUpdateRequest,
    UserUpdateResponse,
)

from src.application.users.commands import (
    UserGetCurrentCommand,
    UserUpdateCurrentCommand,
)
from src.application.users.use_cases import (
    UserGetCurrentUseCase,
    UserUpdateCurrentUseCase,
)
from src.api.dependencies import (
    get_current_user_id,
    get_user_get_current_use_case,
    get_user_update_use_case,
)
from fastapi import HTTPException, status

router = ProtectedAPIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get("/me", response_model=UserMeResponse | None)
async def user_get_current(
        user_id: int = Depends(get_current_user_id),
        use_case: UserGetCurrentUseCase = Depends(get_user_get_current_use_case)
) -> UserMeResponse | None:

    command = UserGetCurrentCommand(
        user_id=user_id,
    )
    print(command.user_id)
    result = await use_case.execute(command)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return UserMeResponse(
        user=result
    )

@router.put("/me", response_model=UserUpdateResponse)
async def user_update_current(
    request: UserUpdateRequest,
    user_id: int = Depends(get_current_user_id),
    use_case: UserUpdateCurrentUseCase = Depends(get_user_update_use_case),
) -> UserUpdateResponse:
    changes = request.model_dump(exclude_unset=True)

    command = UserUpdateCurrentCommand(
        user_id=user_id,
        changes=changes,
    )

    result = await use_case.execute(command)

    return UserUpdateResponse(user=result)
