from typing import List, Dict, Any
from repository.database import connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete


class Repository:
    model = None

    @classmethod
    @connection
    async def insert_many(cls, session: AsyncSession, instances: List[Dict[str, Any]]):
        new_instances = [cls.model(**values) for values in instances]
        session.add_all(new_instances)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instances

    @classmethod
    @connection
    async def insert(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    @connection
    async def update(cls, session: AsyncSession, filters: Dict[str, Any], values: Dict[str, Any]):
        stmt = (
            update(cls.model)
            .where(*[getattr(cls.model, key) == value for key, value in filters.items()])
            .values(**values)
            .execution_options(synchronize_session="fetch")
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount

    @classmethod
    @connection
    async def delete(cls, session: AsyncSession, **filters: Dict[str, Any]):
        stmt = (
            delete(cls.model)
            .where(*[getattr(cls.model, key) == value for key, value in filters.items()])
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount


    @classmethod
    @connection
    async def get_all(cls, session: AsyncSession):
        stmt = select(cls.model)
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records


    @classmethod
    @connection
    async def get_by_primary_key(cls, session: AsyncSession, **keys):
        stmt = (
            select(cls.model)
            .where(*[getattr(cls.model, key) == value for key, value in keys.items()])
        )
        result = await session.execute(stmt)
        record = result.unique().scalar_one_or_none()
        return record


    @classmethod
    @connection
    async def find(cls, session: AsyncSession, **filters):
        stmt = (
            select(cls.model)
            .where(*[getattr(cls.model, key) == value for key, value in filters.items()])
        )
        result = await session.execute(stmt)
        records = result.unique().scalars().all()
        return records