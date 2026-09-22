from src.application.interfaces import (
    RidesRepository,
    RouteService,
)
from src.application.rides.commands import RideActiveCommand
from src.domain.entities import Ride
from src.domain.value_objects import Route


class RideActiveUseCase:

    def __init__(
            self,
            route_service: RouteService,
            ride_repository: RidesRepository,
    ):
        self._route_service = route_service
        self._ride_repository = ride_repository

    async def execute(
            self,
            command: RideActiveCommand,
    ) -> tuple[Ride, Route] | None:
        ride = await self._ride_repository.get_active_by_user_id(command.user_id)

        if not ride:
            return None

        route = await self._route_service.calculate_route(
            pickup=ride.pickup_geo,
            destination=ride.destination_geo,
        )

        return ride, route
