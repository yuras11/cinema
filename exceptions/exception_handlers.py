from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from urllib.parse import quote
from exceptions.exceptions import AppException, NotFoundException, AlreadyExistsException, SeatException

templates = Jinja2Templates(directory="templates")


def register_exception_handlers(app):

    def redirection(exc, status_code):
        message = quote(exc.get_message())
        return RedirectResponse(
            url=f"/pages/error/404?message={message}",
            status_code=status_code
        )

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return redirection(exc=exc, status_code=400)


    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return redirection(exc=exc, status_code=404)


    @app.exception_handler(AlreadyExistsException)
    async def already_exists_handler(request: Request, exc: AlreadyExistsException):
        return redirection(exc=exc, status_code=303)

    @app.exception_handler(SeatException)
    async def seat_exception(request: Request, exc: SeatException):
        return redirection(exc=exc, status_code=409)