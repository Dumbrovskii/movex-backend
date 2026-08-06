from pydantic import BaseModel, Field

class RequestCodeRequest(BaseModel):
    phone: str = Field(
        ...,
        pattern=r"^\+[1-9]\d{7,14}$",
        examples=["+380991234567"],
        description="Phone number in E.164 format.",
    )

class RequestCodeResponse(BaseModel):
    success: bool

class VerifyCodeRequest(BaseModel):
    phone: str = Field(
        ...,
        pattern=r"^\+[1-9]\d{7,14}$",
        examples=["+380991234567"],
    )

    code: str = Field(
        ...,
        pattern=r"^\d{6}$",
        examples=["123456"],
    )

class VerifyCodeResponse(BaseModel):
    access_token: str
    refresh_token: str