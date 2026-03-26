from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.cast_member_model import CastMemberModel
from database import connection
from api.comands.cast_member.cast_member_command import CastMemberCommand


class UpdateCastMemberCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, memberid: int, command: CastMemberCommand):
        stmt = (
            select(CastMemberModel)
            .where(CastMemberModel.memberid == memberid)
        )
        existing = await session.execute(stmt)
        cast_member = existing.unique().scalar_one_or_none()

        if cast_member is None:
            return None

        cast_member.membername = command.membername
        cast_member.dateofbirth = command.dateofbirth
        cast_member.countrycode = command.countrycode
        cast_member.professionid = command.professionid

        try:
            await session.commit()
            await session.refresh(cast_member)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return cast_member