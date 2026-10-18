from abc import ABC, abstractmethod
from movex_domain.value_objects.geo_point import GeoPoint
from movex_domain.value_objects.route import Route


class RouteService(ABC):

    @abstractmethod
    async def calculate_route(
            self,
            pickup: GeoPoint,
            destination: GeoPoint,
    ) -> Route:
        pass