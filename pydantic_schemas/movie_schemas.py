import datetime
import uuid

from pydantic import BaseModel, Field
from typing import List
from datetime import timedelta, date
from pydantic_schemas.country_schemas import CountryScheme


class MovieNameScheme(BaseModel):
    movieid: uuid.UUID
    languagecode: str
    moviename: str
    model_config = {'from_attributes': True}


class GenreNameScheme(BaseModel):
    genreid: uuid.UUID
    languagecode: str
    genrename: str
    model_config = {'from_attributes': True}


class GenreScheme(BaseModel):
    genreid: uuid.UUID
    model_config = {'from_attributes': True}
    names: List["GenreNameScheme"]
    model_config = {'from_attributes': True}


class MovieScheme(BaseModel):
    movieid: uuid.UUID
    names: List["MovieNameScheme"]
    durationtime: timedelta
    agerate: str = Field(pattern=r"^\d{1,2}\+$", description="Age rate should be in a proper format")
    releasedate: date
    countries: List["CountryScheme"]
    genres: List["GenreScheme"]
    cast: List["CastMemberScheme"]
    model_config = {'from_attributes': True}


