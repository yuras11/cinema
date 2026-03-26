import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from orm.hall_model import SeatStatusModel
from api.comands.cinema_session.cinema_session_command import SeatBookingRequest
from database import connection


class CancelBookingCinemaSessionTicketCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls,
                           session: AsyncSession,
                           sessionid: int,
                           command: SeatBookingRequest,
                           userid: uuid.UUID):
        stmt = (
            select(SeatStatusModel).where(
                SeatStatusModel.sessionid == sessionid,
                SeatStatusModel.rownumber == command.rownumber,
                SeatStatusModel.seatnumber == command.seatnumber,
                SeatStatusModel.userid == userid)
        )

        result = await session.execute(stmt)
        seat_status = result.unique().scalar_one_or_none()

        if not seat_status:
            return False

        seat_status.userid = None
        session.add(seat_status)

        await session.commit()
        return True