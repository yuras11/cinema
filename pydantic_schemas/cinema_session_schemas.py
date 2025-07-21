import datetime
import uuid

from pydantic import BaseModel, Field
from typing import List

from pydantic_schemas.hall_schemas import HallScheme
from pydantic_schemas.movie_schemas import MovieScheme


class CinemaSessionScheme(BaseModel):
    movieid: uuid.UUID
    hallid: uuid.UUID
    sessiondate: datetime.date
    sessiontime: datetime.timedelta
    ticketfee: float
    currencycode: str
    model_config = {'from_attributes': True}