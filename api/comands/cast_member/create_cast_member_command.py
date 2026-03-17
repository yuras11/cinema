from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel, Field
from orm.cast_member_model import CastMemberModel
from repository.database import connection
import datetime
from api.comands.cast_member.cast_member_command import CastMemberCommand


class CreateCastMemberCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: CastMemberCommand):
        stmt = (
            select(CastMemberModel)
            .where(CastMemberModel.membername == command.membername)
        )
        existing = await session.execute(stmt)
        if existing.unique().scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f'Cast member with name {command.membername} already exists!')

        model = CastMemberModel(**command.model_dump())
        session.add(model)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return model