from repository.repos import CountryRepository
from pydantic_schemas.country_schemas import CountryScheme


class CountryService:
    @classmethod
    async def get_all_countries(cls):
        return await CountryRepository.get_all()


    @classmethod
    async def create_country(cls, country: CountryScheme):
        return await CountryRepository.insert(**country.model_dump())


    @classmethod
    async def delete_country(cls, countrycode: str):
        return await CountryRepository.delete(countrycode=countrycode)
