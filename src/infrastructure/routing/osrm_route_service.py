import httpx

from src.application.interfaces.services import RouteService
from src.domain.value_objects import GeoPoint, Route

from src.config import settings


class OSRMRouteService(RouteService):

    def __init__(self, osrm_url: str, client: httpx.AsyncClient):
        self._osrm_url = osrm_url
        self._client = client

    async def calculate_route(
            self,
            pickup: GeoPoint,
            destination: GeoPoint
    ) -> Route:
        url = (
            f"{settings.OSRM_HOST}/route/v1/driving/"
            f"{pickup.longitude},{pickup.latitude};"
            f"{destination.longitude},{destination.latitude}"
        )

        response = await self._client.get(
            url,
            params={
                "overview": "full",
                "geometries": "geojson",
            }
        )
        response.raise_for_status()

        data = response.json()
        route = data["routes"][0]

        geometry = [
            GeoPoint(latitude=lat, longitude=lon)
            for lon, lat in route["geometry"]["coordinates"]
        ]

        waypoints = [
            GeoPoint(latitude=lat, longitude=lon)
            for waypoint in data["waypoints"]
            for lon, lat in [waypoint["location"]]
        ]

        return Route(
            distance_meters=route["distance"],
            duration_seconds=route["duration"],
            geometry=geometry,
            waypoints=waypoints,
        )