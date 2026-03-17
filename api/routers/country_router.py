from fastapi import APIRouter
from api.comands.country.create_country_command import CreateCountryCommandHandler
from api.comands.country.delete_country_command import DeleteCountryCommandHandler
from api.comands.country.update_country_command import UpdateCountryCommandHandler
from api.queries.country.get_all_countries_query import GetAllCountriesQueryHandler
from api.queries.country.get_country_by_id_query import GetCountryByIdQueryHandler
from api.comands.country.country_command import CountryCommand


country_router = APIRouter(prefix='/countries', tags=["Countries"])

@country_router.get('/')
async def get_all_countries():
    countries = await GetAllCountriesQueryHandler.handle_async()
    return [country.to_dict() for country in countries]


@country_router.get('/{countryid}')
async def get_country_by_id(countryid: str):
    country = await GetCountryByIdQueryHandler.handle_async(countrycode=countryid)
    return country.to_dict()


@country_router.post('/')
async def create_country(country: CountryCommand):
    result = await CreateCountryCommandHandler.handle_async(command=country)
    return {'message': "Country is successfully created"} if result else {'message': 'error'}


@country_router.put('/{countryid}')
async def update_country(countryid: str, command: CountryCommand):
    result = await UpdateCountryCommandHandler.handle_async(countrycode=countryid, command=command)
    return {'message': "Country is successfully updated"} if result else {'message': 'error'}


@country_router.delete('/{countryid}')
async def delete_country(countryid: str):
    result = await DeleteCountryCommandHandler.handle_async(countrycode=countryid)
    return {'message': "Country is successfully deleted"} if result else {'message': 'error'}