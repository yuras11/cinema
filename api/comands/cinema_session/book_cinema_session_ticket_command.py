from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from dependencies import get_current_user
from orm.hall_model import SeatStatusModel
from orm.user_model import UserModel
from api.comands.cinema_session.cinema_session_command import SeatBookingRequest
from repository.database import connection


class BookCinemaSessionTicketCommandHandler:
    @classmethod
    @connection
    async def handle_async(cls,
                      session: AsyncSession,
                      sessionid: int,
                      command: SeatBookingRequest,
                      user: UserModel):
        stmt = (
            select(SeatStatusModel)
            .where(
                SeatStatusModel.sessionid == sessionid,
                SeatStatusModel.rownumber == command.rownumber,
                SeatStatusModel.seatnumber == command.seatnumber,
            )
        )

        result = await session.execute(stmt)
        seat_status = result.unique().scalar_one_or_none()

        if seat_status is None:
            return False

        if seat_status.userid is not None:
            return False

        seat_status.userid = user.userid
        session.add(seat_status)

        await session.commit()
        return True