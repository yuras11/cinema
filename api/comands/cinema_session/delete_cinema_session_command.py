from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from orm.cinema_session_model import CinemaSessionModel
from database import connection


class DeleteCinemaSessionCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, sessionid: int):
        stmt = (
            delete(CinemaSessionModel)
            .where(CinemaSessionModel.sessionid == sessionid)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount