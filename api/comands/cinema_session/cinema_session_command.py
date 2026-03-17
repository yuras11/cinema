from pydantic import BaseModel, Field
import datetime


class CinemaSessionCommand(BaseModel):
    movieid: int
    hallid: int
    sessiondate: datetime.date
    sessiontime: datetime.timedelta
    ticketfee: float
    currencycode: str
    model_config = {'from_attributes': True}


class SeatBookingRequest(BaseModel):
    rownumber: int
    seatnumber: int
    model_config = {'from_attributes': True}