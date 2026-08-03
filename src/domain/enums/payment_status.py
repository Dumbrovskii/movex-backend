from enum import Enum, auto

class PaymentStatus(Enum):
    PENDING = auto()
    AUTHORIZED = auto()
    PAID = auto()
    FAILED = auto()
    REFUNDED = auto()