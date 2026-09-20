class ActiveRideExistsError(Exception):

    def __init__(self) -> None:
        super().__init__("User already has an active ride.")
