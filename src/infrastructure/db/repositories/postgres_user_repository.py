from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces import UserRepository
from movex_domain.entities.user import User
from src.infrastructure.db.mappers import UserMapper
from src.infrastructure.db.models import UserModel


class PostgresUserRepository(UserRepository):

    def __init__(
            self,
            session: AsyncSession,
    ) -> None:
        self._session = session

    async def get_by_id(
            self,
            user_id: int,
    ) -> User | None:

        model = await self._session.scalar(
            select(UserModel).where(
                UserModel.id == user_id,
                UserModel.deleted_at.is_(None),
            )
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)

    async def get_by_phone(
            self,
            phone: str,
    ) -> User | None:

        model = await self._session.scalar(
            select(UserModel).where(
                UserModel.phone == phone,
                UserModel.deleted_at.is_(None),
            )
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)

    async def create(
            self,
            phone: str,
    ) -> User:

        model = UserModel(
            phone=phone,
            full_name=None,
            email=None,
        )

        self._session.add(model)

        await self._session.commit()
        await self._session.refresh(model)

        return UserMapper.to_domain(model)

    async def get_or_create(
            self,
            phone: str,
    ) -> User:

        user = await self.get_by_phone(phone)

        if user is not None:
            return user

        return await self.create(phone)

    async def update(
            self,
            user_id: int,
            changes: dict[str, str | None],
    ) -> User:
        stmt = (
            update(UserModel)
            .where(UserModel.id == user_id)
            .values(**changes)
            .returning(UserModel)
        )

        result = await self._session.execute(stmt)
        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise Exception(user_id)

        await self._session.commit()

        print(UserMapper.to_domain(user_model).full_name)

        return UserMapper.to_domain(user_model)
