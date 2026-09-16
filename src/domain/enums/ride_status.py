from enum import Enum, auto

class RideStatus(Enum):
    REQUESTED = auto()
    ACCEPTED = auto()
    DRIVER_ARRIVING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELED = auto()