from pydantic import BaseModel, Field
import datetime


class CastMemberCommand(BaseModel):
    membername: str
    dateofbirth: datetime.date
    countrycode: str = Field(min_length=2, max_length=2)
    professionid: int
    model_config = {'from_attributes': True}