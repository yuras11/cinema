from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from urllib.parse import quote
from exceptions.exceptions import AppException, NotFoundException, AlreadyExistsException

templates = Jinja2Templates(directory="templates")


def register_exception_handlers(app):

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        if request.url.path.startswith("/api"):
            return JSONResponse(
                status_code=400,
                content={"message": exc.get_message()}
            )

        return templates.TemplateResponse(
            "errors/404.html",
            {"request": request, "message": exc.get_message()},
            status_code=400
        )


    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return templates.TemplateResponse(
            "errors/404.html",
            {"request": request, "message": exc.get_message()},
            status_code=404
        )


    @app.exception_handler(AlreadyExistsException)
    async def already_exists_handler(request: Request, exc: AlreadyExistsException):
        message = quote(exc.get_message())
        return RedirectResponse(
            url=f"/pages/error/404?message={message}",
            status_code=303
        )
