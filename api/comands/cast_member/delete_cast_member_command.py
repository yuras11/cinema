from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.cast_member_model import CastMemberModel
from database import connection


class DeleteCastMemberCommandHandler:

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, memberid: int):
        stmt = (
            delete(CastMemberModel)
            .where(CastMemberModel.memberid == memberid)
        )
        try:
            result = await session.execute(stmt)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return result.rowcount
