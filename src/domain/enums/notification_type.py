from enum import Enum, auto

class NotificationType(Enum):
    RIDE_REQUESTED = auto()
    RIDE_ACCEPTED = auto()
    RIDE_STARTED = auto()
    RIDE_COMPLETED = auto()
    RIDE_CANCELED = auto()

    PAYMENT_SUCCEEDED = auto()
    PAYMENT_FAILED = auto()