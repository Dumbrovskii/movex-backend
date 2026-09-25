from sqlalchemy import select, exists, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces import RidesRepository
from src.domain.entities import Ride
from src.domain.enums import RideStatus
from src.infrastructure.db.mappers.ride_mapper import RideMapper
from src.infrastructure.db.models.ride_model import RideModel


class PostgresRidesRepository(RidesRepository):

    def __init__(
            self,
            session: AsyncSession,
    ) -> None:
        self._session = session

    async def create(self, ride: Ride) -> Ride:
        model = RideMapper.to_model(ride)

        self._session.add(model)

        await self._session.commit()
        await self._session.refresh(model)

        return RideMapper.to_domain(model)

    async def get_by_id(self, ride_id: int) -> Ride | None:
        model = await self._session.scalar(
            select(RideModel).where(
                RideModel.id == ride_id,
            )
        )

        if model is None:
            return None

        return RideMapper.to_domain(model)


    async def update(self, ride: Ride) -> Ride:
        pass


    async def cancel(self, user_id: int, ride_id: int) -> bool:
        stmt = (
            update(RideModel)
            .where(RideModel.passenger_id == user_id,
                   RideModel.id == ride_id)
            .values(
                status=RideStatus.CANCELED,
            )
            .returning(RideModel.id)
        )

        result = await self._session.execute(stmt)
        await self._session.commit()

        return result.scalar_one_or_none() is not None


    async def get_active_by_user_id(self, user_id: int) -> Ride | None:
        stmt = (
            select(RideModel)
            .where(
                RideModel.passenger_id == user_id,
                RideModel.status.in_([
                    RideStatus.REQUESTED,
                    RideStatus.ACCEPTED,
                    RideStatus.IN_PROGRESS,
                ]),
            )
            .order_by(RideModel.created_at.desc())
            .limit(1))

        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return RideMapper.to_domain(model)


    async def update_status(self, ride_id: int, status: RideStatus) -> None:
        pass


    async def assign_driver(self, ride_id: int, drive_id: int) -> None:
        pass


    async def exists_active_by_user_id(self, user_id: int) -> bool:
        query = select(
            exists().where(
                RideModel.passenger_id == user_id,
                RideModel.status.notin_([
                    RideStatus.COMPLETED,
                    RideStatus.CANCELED,
                ])
            )
        )

        result = await self._session.execute(query)
        return result.scalar_one()
