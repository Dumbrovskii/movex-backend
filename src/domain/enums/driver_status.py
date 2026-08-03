from enum import Enum, auto

class DriverStatus(Enum):
    PENDING = auto()
    VERIFIED = auto()
    SUSPENDED = auto()
