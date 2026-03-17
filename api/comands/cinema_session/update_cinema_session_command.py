from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from orm.cinema_session_model import CinemaSessionModel
from api.comands.cinema_session.cinema_session_command import CinemaSessionCommand
from orm.hall_model import HallModel, SeatStatusModel
from repository.database import connection


class UpdateCinemaSessionCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, sessionid: int, command: CinemaSessionCommand):
        result = await session.execute(
            select(CinemaSessionModel).where(CinemaSessionModel.sessionid == sessionid)
        )
        cinema_session = result.unique().scalar_one_or_none()

        if cinema_session is None:
            return None

        result = await session.execute(
            select(HallModel).where(HallModel.hallid == cinema_session.hallid)
        )
        cinema_session.hall = result.unique().scalar_one_or_none()

        result = await session.execute(
            select(HallModel).where(HallModel.hallid == command.hallid)
        )
        hall = result.unique().scalar_one_or_none()

        await session.execute(
            delete(SeatStatusModel).where(
                SeatStatusModel.hallid == cinema_session.hallid,
                SeatStatusModel.sessionid == cinema_session.sessionid
            )
        )

        cinema_session.movieid = command.movieid
        cinema_session.hallid = command.hallid
        cinema_session.sessiondate = command.sessiondate
        cinema_session.sessiontime = command.sessiontime
        cinema_session.ticketfee = command.ticketfee
        cinema_session.currencycode = command.currencycode

        for row in range(1, hall.rowamount + 1):
            for seat in range(1, hall.seatamount + 1):
                seat_status = SeatStatusModel(
                    sessionid=sessionid,
                    hallid=command.hallid,
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