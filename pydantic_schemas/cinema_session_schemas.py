import datetime
from pydantic import BaseModel


class CinemaSessionCreateScheme(BaseModel):
    movieid: int
    hallid: int
    sessiondate: datetime.date
    sessiontime: datetime.timedelta
    ticketfee: float
    currencycode: str

    model_config = {'from_attributes': True}


class CinemaSessionUpdateScheme(BaseModel):
    sessionid: int
    movieid: int
    hallid: int
    sessiondate: datetime.date
    sessiontime: datetime.timedelta
    ticketfee: float
    currencycode: str

    model_config = {'from_attributes': True}
