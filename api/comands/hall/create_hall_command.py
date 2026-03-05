from orm.hall_model import HallModel, SeatModel
from pydantic_schemas.hall_schemas import HallCommand
from repository.database import connection
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


class CreateHallCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: HallCommand):
        stmt = (
            select(HallModel)
            .where(HallModel.hallname == command.hallname)
        )
        existing = await session.execute(stmt)
        if existing.unique().scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f'Hall with name {command.hallname} already exists!')

        hall = HallModel(**command.model_dump())
        session.add(hall)
        await session.flush()  # this is for getting hall's id before commiting to DB

        for row in range(command.rowamount):
            for seat in range(command.seatamount):
                seat_model = SeatModel(
                    hallid=hall.hallid,
                    rownumber=row + 1,
                    seatnumber=seat + 1
                )
                session.add(seat_model)

        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return hall