import httpx
from fastapi import Depends

from src.api.dependencies.providers import get_http_client
from src.application.interfaces import RouteService, PricingService
from src.application.rides.use_cases import EstimateRideUseCase
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


async def get_estimate_ride_use_cases(
        route_service: RouteService = Depends(get_route_service),
        pricing_service: PricingService = Depends(get_price_service),

) -> EstimateRideUseCase:
    return EstimateRideUseCase(
        route_service=route_service,
        pricing_service=pricing_service
    )