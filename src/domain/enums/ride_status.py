from enum import Enum, auto

class RideStatus(Enum):
    REQUESTED = auto()
    ACCEPTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELED = auto()