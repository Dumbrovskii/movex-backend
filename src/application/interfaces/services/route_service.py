from abc import ABC, abstractmethod
from src.domain.value_objects import GeoPoint, Route


class RouteService(ABC):

    @abstractmethod
    async def calculate_route(
            self,
            pickup: GeoPoint,
            destination: GeoPoint,
    ) -> Route:
        pass