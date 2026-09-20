from abc import ABC, abstractmethod

from src.domain.entities.ride import Ride, RideStatus

class RidesRepository(ABC):

    @abstractmethod
    async def create(self,  ride: Ride) -> Ride:
        pass

    @abstractmethod
    async def get_by_id(self, ride_id: int) -> Ride | None:
        pass

    @abstractmethod
    async def update(self, ride: Ride) -> Ride:
        pass

    @abstractmethod
    async def get_active_by_user_id(self, user_id: int) -> Ride | None:
        pass

    @abstractmethod
    async def update_status(self, ride_id: int, status: RideStatus) -> None:
        pass

    @abstractmethod
    async def assign_driver(self, ride_id: int, drive_id: int) -> None:
        pass

    @abstractmethod
    async def exists_active_by_user_id(self, user_id: int ) -> bool:
        pass