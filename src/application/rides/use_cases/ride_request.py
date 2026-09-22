from src.application.interfaces import (
    RouteService,
    PricingService,
    RidesRepository,
)
from src.application.exceptions import (
    ActiveRideExistsError,
)
from src.application.rides.commands import RideRequestCommand
from src.domain.value_objects import Route, Money
from src.domain.entities import Ride
from src.domain.enums import RideStatus


class RideRequestUseCase:

    def __init__(
            self,
            route_service: RouteService,
            pricing_service: PricingService,
            rides_repository: RidesRepository,
    ):
        self._route_service = route_service
        self._pricing_service = pricing_service
        self._rides_repository = rides_repository

    async def execute(
            self,
            command: RideRequestCommand,
    ) -> tuple[Route, Money]:

        exists_ride = await self._rides_repository.exists_active_by_user_id(command.user_id)

        if exists_ride:
            raise ActiveRideExistsError()

        route = await self._route_service.calculate_route(
            pickup=command.pickup,
            destination=command.destination,
        )

        price = self._pricing_service.calculate_price(route)

        ride = Ride(
            passenger_id=command.user_id,
            pickup_address='',
            pickup_geo=command.pickup,
            destination_address='',
            destination_geo=command.destination,
            status=RideStatus.REQUESTED,
            distance_meters=route.distance_meters,
            price=price.amount,
            currency=price.currency,
        )

        await self._rides_repository.create(ride)

        return route, price
