from fastapi import Depends, Response

from src.api.contracts import (
    RideEstimateRequest,
    RideEstimateResponse,
    RideRequest,
    RideResponse,
    RideActiveResponse, RideCancelRequest,
)
from src.api.dependencies import (
    get_ride_estimate_use_case,
    get_ride_request_use_case,
    get_ride_active_use_case,
    get_ride_cancel_use_case,
    get_current_user_id,
)
from src.api.routing import ProtectedAPIRouter
from src.application.rides.commands import (
    RideEstimateCommand,
    RideRequestCommand,
    RideActiveCommand,
    RideCancelCommand,
)
from src.application.rides.use_cases import (
    RideEstimateUseCase,
    RideRequestUseCase,
    RideActiveUseCase, RideCancelUseCase,
)
from src.domain.value_objects import GeoPoint

router = ProtectedAPIRouter(
    prefix="/rides",
    tags=["Rides"],
)

@router.post("/estimate", response_model=RideEstimateResponse)
async def ride_estimate(
        request: RideEstimateRequest,
        use_case: RideEstimateUseCase = Depends(get_ride_estimate_use_case)
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
async def ride_request(
        request: RideRequest,
        user_id: int = Depends(get_current_user_id),
        use_case: RideRequestUseCase = Depends(get_ride_request_use_case),
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

    route, ride = await use_case.execute(command)

    return RideResponse(
        ride=ride,
        route=route,
    )

@router.get("/active", response_model=RideActiveResponse | None)
async def ride_active(
        response: Response,
        user_id: int = Depends(get_current_user_id),
        use_case: RideActiveUseCase = Depends(get_ride_active_use_case)
) -> RideActiveResponse | None:

    command = RideActiveCommand(
        user_id=user_id,
    )

    result = await use_case.execute(command)

    if result is None:
        response.status_code = 204
        return None

    ride, route = result

    return RideActiveResponse(
        route=route,
        ride=ride,
    )

@router.delete("/cancel", status_code=204)
async def ride_cancel(
        request: RideCancelRequest,
        user_id: int = Depends(get_current_user_id),
        use_case: RideCancelUseCase = Depends(get_ride_cancel_use_case)
) -> None:

    command = RideCancelCommand(
        user_id=user_id,
        ride_id=request.ride_id,
    )

    await use_case.execute(command)
