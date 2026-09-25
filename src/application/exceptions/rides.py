class ActiveRideExistsError(Exception):

    def __init__(self) -> None:
        super().__init__("User already has an active ride.")

class RideNotFoundError(Exception):

    def __init__(self) -> None:
        super().__init__("Ride not found.")
