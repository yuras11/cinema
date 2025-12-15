import datetime
import uuid

from pydantic import BaseModel, Field
from typing import List
from datetime import timedelta, date
from pydantic_schemas.country_schemas import CountryScheme
from pydantic_schemas.cast_member_schemas import CastMemberUpdateScheme


class MovieScheme(BaseModel):
    moviename: str
    durationtime: timedelta
    agerate: str = Field(pattern=r"^\d{1,2}\+$", description="Age rate should be in a proper format")
    releaseyear: int
    genres: List[int]
    cast: List[int]
    countries: List[str]

    model_config = {'from_attributes': True}


class MovieUpdateScheme(BaseModel):
    movieid: int
    moviename: str
    durationtime: timedelta
    agerate: str = Field(pattern=r"^\d{1,2}\+$", description="Age rate should be in a proper format")
    releaseyear: int
    genres: List[int]
    cast: List[int]
    countries: List[str]

    model_config = {'from_attributes': True}


class MovieGetAllScheme(BaseModel):
    movieid: int
    moviename: str
    durationtime: timedelta
    agerate: str = Field(pattern=r"^\d{1,2}\+$", description="Age rate should be in a proper format")
    releaseyear: int

    model_config = {'from_attributes': True}