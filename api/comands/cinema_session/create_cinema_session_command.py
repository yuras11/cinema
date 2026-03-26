from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from orm.cinema_session_model import CinemaSessionModel
from orm.hall_model import HallModel, SeatStatusModel
from api.comands.cinema_session.cinema_session_command import CinemaSessionCommand
from database import connection


class CreateCinemaSessionCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: CinemaSessionCommand):
        cinema_session = CinemaSessionModel(**command.model_dump())
        result = await session.execute(
            select(HallModel).where(HallModel.hallid == command.hallid)
        )
        cinema_session.hall = result.unique().scalar_one_or_none()
        session.add(cinema_session)
        await session.flush()

        for row in range(1, cinema_session.hall.rowamount + 1):
            for seat in range(1, cinema_session.hall.seatamount + 1):
                seat_status = SeatStatusModel(
                    sessionid=cinema_session.sessionid,
                    hallid=cinema_session.hallid,
                    rownumber=row,
                    seatnumber=seat
                )
                session.add(seat_status)

        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return cinema_session