from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import JSONResponse

from src.application.exceptions import (
    ActiveRideExistsError,
    RideNotFoundError,
)

def register_rides_exceptions_handlers(app: FastAPI) -> None:

    @app.exception_handler(ActiveRideExistsError)
    async def active_ride_exist_handler(
            request: Request,
            exc: ActiveRideExistsError,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "error": {
                    "code": "ACTIVE_RIDE_EXISTS",
                    "message": str(exc),
                },
            },
        )

    @app.exception_handler(RideNotFoundError)
    async def ride_not_found_handler(
            request: Request,
            exc: RideNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                    "code": "RIDE_NOT_FOUND",
                    "message": str(exc),
                },
            },
        )
