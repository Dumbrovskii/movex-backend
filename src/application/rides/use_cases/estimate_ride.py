from src.application.interfaces.services import RouteService, PricingService
from src.application.rides.commands.estimate_ride import EstimateRideCommand
from src.domain.value_objects import Route, Money


class EstimateRideUseCase:

    def __init__(
            self,
            route_service: RouteService,
            pricing_service: PricingService,
    ):
        self._route_service = route_service
        self._pricing_service = pricing_service

    async def execute(
            self,
            command: EstimateRideCommand
    ) -> tuple[Route, Money]:
        route = await self._route_service.calculate_route(
            pickup=command.pickup,
            destination=command.destination,
        )

        price = self._pricing_service.calculate_price(route)

        return route, price
