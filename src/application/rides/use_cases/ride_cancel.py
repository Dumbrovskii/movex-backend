from src.application.exceptions import RideNotFoundError
from src.application.interfaces import RidesRepository
from src.application.rides.commands import RideCancelCommand


class RideCancelUseCase:

    def __init__(
            self,
            rides_repository: RidesRepository
    ):
        self._rides_repository = rides_repository

    async def execute(
            self,
            command: RideCancelCommand
    ):

        is_canceled = await self._rides_repository.cancel(
            user_id=command.user_id,
            ride_id=command.ride_id,
        )

        if not is_canceled:
            raise RideNotFoundError()
