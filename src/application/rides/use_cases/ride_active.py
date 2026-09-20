from src.application.interfaces import RidesRepository
from src.application.rides.commands import RideActiveCommand
from src.domain.entities import Ride


class RideActiveUseCase:

    def __init__(
            self,
            ride_repository: RidesRepository,
    ):
        self._ride_repository = ride_repository

    async def execute(
            self,
            command: RideActiveCommand,
    ) -> Ride | None:

        return await self._ride_repository.get_active_by_user_id(command.user_id)
