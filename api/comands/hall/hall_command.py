from pydantic import BaseModel, Field


class HallCommand(BaseModel):
    hallname: str
    seatamount: int = Field(le=20)  # amount of seats in a single row
    rowamount: int = Field(le=20)