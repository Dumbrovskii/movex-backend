from src.application.interfaces.services import RouteService, PricingService
from src.application.rides.commands.ride_estimate import RideEstimateCommand
from movex_domain.value_objects.route import Route
from movex_domain.value_objects.money import Money


class RideEstimateUseCase:

    def __init__(
            self,
            route_service: RouteService,
            pricing_service: PricingService,
    ):
        self._route_service = route_service
        self._pricing_service = pricing_service

    async def execute(
            self,
            command: RideEstimateCommand
    ) -> tuple[Route, Money]:
        route = await self._route_service.calculate_route(
            pickup=command.pickup,
            destination=command.destination,
        )

        price = self._pricing_service.calculate_price(route)

        return route, price

