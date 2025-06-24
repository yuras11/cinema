import datetime
import uuid

from pydantic import BaseModel, Field
from typing import List
from pydantic_schemas.country_schemas import CountryScheme


class CastMemberNameScheme(BaseModel):
    memberid: uuid.UUID
    languagecode: str
    membername: str
    model_config = {'from_attributes': True}


class CastMemberScheme(BaseModel):
    memberid: uuid.UUID
    dateofbirth: datetime.date
    countrycode: str = Field(min_length=2, max_length=2)
    country: CountryScheme
    names: List[CastMemberNameScheme]
    positions: List["PositionScheme"]
    model_config = {'from_attributes': True}


class CastMemberCreateScheme(BaseModel):
    memberid: uuid.UUID
    dateofbirth: datetime.date
    countrycode: str = Field(min_length=2, max_length=2)
    names: List[CastMemberNameScheme]
    positions: List["PositionScheme"]
    model_config = {'from_attributes': True}


class PositionNameScheme(BaseModel):
    positionid: uuid.UUID
    languagecode: str = Field(min_length=2, max_length=2)
    positionname: str
    model_config = {'from_attributes': True}


class PositionScheme(BaseModel):
    positionid: uuid.UUID
    names: List[PositionNameScheme]
    #cast_members: List[CastMemberScheme]
    model_config = {'from_attributes': True}
