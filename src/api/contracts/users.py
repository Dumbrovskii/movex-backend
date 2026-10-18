from pydantic import BaseModel
from movex_domain.entities.user import User

class UserMeResponse(BaseModel):
    user: User

class UserMeRequest(BaseModel):
    pass

class UserUpdateResponse(BaseModel):
    user: User

class UserUpdateRequest(BaseModel):
    phone: str
    full_name: str | None
    email: str | None
