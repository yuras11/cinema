from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.user_model import UserModel
from repository.database import connection


class DeleteUserCommandHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, userid: str):
        stmt = (
            delete(UserModel)
            .where(UserModel.userid == userid)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount
