from fastapi import APIRouter, Depends, Response

from src.api.contracts.rides import (
    EstimateRideRequest,
    EstimateRideResponse,
)
from src.api.dependencies import get_estimate_ride_use_cases
from src.application.rides.commands.estimate_ride import EstimateRideCommand
from src.application.rides.use_cases import EstimateRideUseCase
from src.domain.value_objects import GeoPoint

router = APIRouter(
    prefix="/rides",
    tags=["Rides"],
)

@router.post("/estimate", response_model=EstimateRideResponse)
async def estimate_ride(
        request: EstimateRideRequest,
        use_case: EstimateRideUseCase = Depends(get_estimate_ride_use_cases)
) -> EstimateRideResponse:

    command = EstimateRideCommand(
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

    return EstimateRideResponse(
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
