from pydantic import BaseModel, Field


class CountryScheme(BaseModel):
    countrycode: str = Field(min_length=2, max_length=2)
    countryname: str
    model_config = {'from_attributes': True}


class CountryCommand(BaseModel):
    countrycode: str = Field(min_length=2, max_length=2)
    countryname: str
    model_config = {'from_attributes': True}