from .auth import register_auth_exception_handlers
from .rides import register_rides_exceptions_handlers

__all__ = [
    "register_auth_exception_handlers",
    "register_rides_exceptions_handlers",
]