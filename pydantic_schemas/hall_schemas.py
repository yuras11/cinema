import uuid
from uuid import uuid4

from pydantic import BaseModel, Field
from typing import List


class HallNameScheme(BaseModel):
    hallid: uuid.UUID
    languagecode: str
    hallname: str
    model_config = {'from_attributes': True}


class SeatScheme(BaseModel):
    hallid: uuid.UUID
    rownumber: int
    seatnumber: int
    model_config = {'from_attributes': True}


class HallScheme(BaseModel):
    hallid: uuid.UUID
    names: List[HallNameScheme]
    seats: List[SeatScheme]
    model_config = {'from_attributes': True}


class HallCreateScheme(BaseModel):
    hallid: uuid.UUID = Field(default_factory=lambda: uuid4().hex)
    names: List[HallNameScheme]
    seat_amount: int = Field(ge=50)
    row_amount: int = Field(le=20)