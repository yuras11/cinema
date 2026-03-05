from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.hall_model import HallModel
from repository.database import connection


class DeleteHallCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, hallid: int):
        stmt = (
            delete(HallModel)
            .where(HallModel.hallid == hallid)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount