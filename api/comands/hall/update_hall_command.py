from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from orm.hall_model import HallModel, SeatModel
from api.comands.hall.hall_command import HallCommand
from database import connection


class UpdateHallCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, hallid: int, command: HallCommand):
        stmt = (
            select(HallModel)
            .where(HallModel.hallid == hallid)
        )
        existing = await session.execute(stmt)
        hall = existing.unique().scalar_one_or_none()

        if hall is None:
            return None

        hall.hallname = command.hallname

        rows_changed = hall.rowamount != command.rowamount
        seats_changed = hall.seatamount != command.seatamount

        if rows_changed or seats_changed:
            hall.rowamount = command.rowamount
            hall.seatamount = command.seatamount

            await session.execute(
                delete(SeatModel).where(SeatModel.hallid == hall.hallid)
            )

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
            await session.refresh(hall)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return hall