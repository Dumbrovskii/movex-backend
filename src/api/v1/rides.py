from fastapi import Depends

from src.api.contracts import (
    RideEstimateRequest,
    RideEstimateResponse,
    RideRequest,
    RideResponse,
)
from src.api.dependencies import (
    get_estimate_ride_use_cases,
    get_request_ride_use_cases,
    get_current_user_id,
)
from src.api.routing import ProtectedAPIRouter
from src.application.rides.commands import (
    RideEstimateCommand,
    RideRequestCommand,
)
from src.application.rides.use_cases import (
    RideEstimateUseCase,
    RideRequestUseCase,
)
from src.domain.value_objects import GeoPoint

router = ProtectedAPIRouter(
    prefix="/rides",
    tags=["Rides"],
)

@router.post("/estimate", response_model=RideEstimateResponse)
async def estimate_ride(
        request: RideEstimateRequest,
        use_case: RideEstimateUseCase = Depends(get_estimate_ride_use_cases)
) -> RideEstimateResponse:

    command = RideEstimateCommand(
        pickup=GeoPoint(
            latitude=request.pickup_latitude,
            longitude=request.pickup_longitude,
        ),
        destination=GeoPoint(
            latitude=request.destination_latitude,
            longitude=request.destination_longitude,
        )
    )

    route, price = await use_case.execute(command)

    return RideEstimateResponse(
        distance_meters=route.distance_meters,
        duration_seconds=route.duration_seconds,
        geometry=[
            [point.longitude, point.latitude]
            for point in route.geometry
        ],
        waypoints=[
            [point.longitude, point.latitude]
            for point in route.waypoints
        ],
        price=price.amount,
        currency=price.currency,
    )

@router.post("", response_model=RideResponse)
async def request_ride(
        request: RideRequest,
        user_id: int = Depends(get_current_user_id),
        use_case: RideRequestUseCase = Depends(get_request_ride_use_cases),
) -> RideResponse:

    command = RideRequestCommand(
        pickup=GeoPoint(
            latitude=request.pickup_latitude,
            longitude=request.pickup_longitude,
        ),
        destination=GeoPoint(
            latitude=request.destination_latitude,
            longitude=request.destination_longitude,
        ),
        user_id=user_id,
    )

    route, price = await use_case.execute(command)

    return RideResponse(
        distance_meters=route.distance_meters,
        duration_seconds=route.duration_seconds,
        geometry=[
            [point.longitude, point.latitude]
            for point in route.geometry
        ],
        waypoints=[
            [point.longitude, point.latitude]
            for point in route.waypoints
        ],
        price=price.amount,
        currency=price.currency,
    )
