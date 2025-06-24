from pydantic import BaseModel, Field
from typing import List


class CountryNameScheme(BaseModel):
    countrycode: str = Field(min_length=2, max_length=2)
    languagecode: str = Field(min_length=2, max_length=2)
    countryname: str
    model_config = {'from_attributes': True}


class CountryScheme(BaseModel):
    countrycode: str = Field(min_length=2, max_length=2)
    names: List[CountryNameScheme]
    model_config = {'from_attributes': True}
