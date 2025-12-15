import uuid
from uuid import uuid4

from pydantic import BaseModel, Field
from typing import List


class SeatScheme(BaseModel):
    hallid: uuid.UUID
    rownumber: int
    seatnumber: int
    model_config = {'from_attributes': True}


class HallCreateScheme(BaseModel):
    hallname: str
    seatamount: int = Field(le=20) # amount of seats in a single row
    rowamount: int = Field(le=20)


class HallUpdateScheme(BaseModel):
    hallid: int
    hallname: str
    seatamount: int = Field(le=20) # amount of seats in a single row
    rowamount: int = Field(le=20)