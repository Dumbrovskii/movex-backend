import httpx
from fastapi import Depends

from src.api.dependencies.providers import (
    get_http_client,
    get_rides_repository,
)
from src.application.interfaces import (
    RouteService,
    PricingService,
    RidesRepository
)
from src.application.rides.use_cases import (
    RideEstimateUseCase,
    RideRequestUseCase,
    RideActiveUseCase,
)
from src.config.settings import settings
from src.infrastructure.pricing import DefaultPricingService
from src.infrastructure.routing import OSRMRouteService


def get_route_service(
        client: httpx.AsyncClient = Depends(get_http_client),
) -> RouteService:
    return OSRMRouteService(
        osrm_url=settings.OSRM_HOST,
        client=client,
    )


def get_price_service() -> PricingService:
    return DefaultPricingService()


async def get_ride_estimate_use_cases(
        route_service: RouteService = Depends(get_route_service),
        pricing_service: PricingService = Depends(get_price_service),

) -> RideEstimateUseCase:
    return RideEstimateUseCase(
        route_service=route_service,
        pricing_service=pricing_service
    )

async def get_ride_request_use_cases(
        route_service: RouteService = Depends(get_route_service),
        pricing_service: PricingService = Depends(get_price_service),
        rides_repository: RidesRepository = Depends(get_rides_repository),
) -> RideRequestUseCase:
    return RideRequestUseCase(
        route_service=route_service,
        pricing_service=pricing_service,
        rides_repository=rides_repository,
    )

async def get_ride_active_use_cases(
        route_service: RouteService = Depends(get_route_service),
        ride_repository: RidesRepository = Depends(get_rides_repository),
) -> RideActiveUseCase:
    return RideActiveUseCase(
        route_service=route_service,
        ride_repository=ride_repository,
    )
