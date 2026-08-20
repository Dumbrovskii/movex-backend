class InvalidPhoneNumberError(Exception):

    def __init__(self) -> None:
        super().__init__(
            "Invalid phone number."
        )

class TooManyRequestsError(Exception):

    def __init__(self) -> None:
        super().__init__(
            "Verification code was requested too recently."
        )

class InvalidVerificationCodeError(Exception):

    def __init__(self) -> None:
        super().__init__("Invalid verification code.")

class VerificationCodeNotFoundError(Exception):

    def __init__(self) -> None:
        super().__init__("Verification code not found.")

class InvalidRefreshTokenError(Exception):

    def __init__(self) -> None:
        super().__init__("Invalid refresh token.")