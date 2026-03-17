from pydantic import BaseModel, Field
from datetime import timedelta
from typing import List


class MovieCommand(BaseModel):
    moviename: str
    durationtime: timedelta
    agerate: str = Field(pattern=r"^\d{1,2}\+$", description="Age rate should be in a proper format")
    releaseyear: int
    genres: List[int]
    cast: List[int]
    countries: List[str]
    model_config = {'from_attributes': True}