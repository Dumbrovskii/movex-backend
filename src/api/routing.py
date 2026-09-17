from fastapi import APIRouter, Depends

from src.api.dependencies.security import get_current_user_id


class ProtectedAPIRouter(APIRouter):

    def __init__(self, *args, **kwargs):
        kwargs["dependencies"] = [
            Depends(get_current_user_id),
            *kwargs.get("dependencies", []),
        ]
        super().__init__(*args, **kwargs)
