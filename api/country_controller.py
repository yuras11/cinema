from fastapi import APIRouter

from pydantic_schemas.country_schemas import CountryScheme, CountryNameScheme
from service.country_service import CountryService

country_router = APIRouter(prefix='/countries', tags=["Working with countries"])

@country_router.get('/all')
async def get_all_countries():
    countries = await CountryService.get_all_countries()
    return [country.model_dump() for country in [CountryScheme.model_validate(c) for c in countries]]


@country_router.post('/create')
async def create_country(country: CountryScheme):
    result = await CountryService.create_country(country_model=country)
    return {"message": 'Country has been created'} if result else {'message': 'error'}


@country_router.put('/add_name')
async def add_name_to_existing_country(country_name: CountryNameScheme):
    result = await CountryService.add_name_to_existing_country(country_name=country_name)
    return {"message": 'Country has been updated'} if result else {'message': 'error'}


@country_router.put('/update_name')
async def update_country_name(country_name: CountryNameScheme):
    result = await CountryService.update_country_name(country_name=country_name)
    return {"message": 'Country has been updated'} if result else {'message': 'error'}


@country_router.delete('/delete_country')
async def delete_country(countrycode: str):
    result = await CountryService.delete_country(countrycode=countrycode)
    return {"message": 'Country has been deleted'} if result else {'message': 'error'}