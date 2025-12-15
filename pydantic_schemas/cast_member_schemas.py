import datetime
from pydantic import BaseModel, Field


class CastMemberCreateScheme(BaseModel):
    membername: str
    dateofbirth: datetime.date
    countrycode: str
    professionid: int
    model_config = {'from_attributes': True}



class CastMemberUpdateScheme(BaseModel):
    memberid: int
    membername: str
    dateofbirth: datetime.date
    countrycode:  str = Field(min_length=2, max_length=2)
    professionid: int
    model_config = {'from_attributes': True}