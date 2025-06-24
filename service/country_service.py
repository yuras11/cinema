from repository.repos import CountryRepository
from pydantic_schemas.country_schemas import CountryScheme, CountryNameScheme


class CountryService:
    @classmethod
    async def get_all_countries(cls):
        return await CountryRepository.get_all()


    @classmethod
    async def create_country(cls, country_model: CountryScheme):
        return await CountryRepository.insert(country_model=country_model)


    @classmethod
    async def add_name_to_existing_country(cls, country_name: CountryNameScheme):
        return await CountryRepository.add_name(country_name=country_name)


    @classmethod
    async def update_country_name(cls, country_name: CountryNameScheme):
        return await CountryRepository.update_name(country_name_scheme=country_name)


    @classmethod
    async def delete_country(cls, countrycode: str):
        return await CountryRepository.delete(countrycode=countrycode)
