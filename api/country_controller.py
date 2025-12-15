from fastapi import APIRouter

from pydantic_schemas.country_schemas import CountryScheme
from service.country_service import CountryService

country_router = APIRouter(prefix='/countries', tags=["Working with countries"])

@country_router.get('/all')
async def get_all_countries():
    countries = await CountryService.get_all_countries()
    return countries


@country_router.post('/create')
async def create_country(country: CountryScheme):
    result = await CountryService.create_country(country=country)
    return {"message": 'Country has been created'} if result else {'message': 'error'}


@country_router.delete('/delete')
async def delete_country(countrycode: str):
    result = await CountryService.delete_country(countrycode=countrycode)
    return {"message": 'Country has been deleted'} if result else {'message': 'error'}