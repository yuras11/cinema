from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from orm.user_model import UserModel
from pydantic_schemas.user_schemas import UserCommand
from repository.database import connection


class CreateUserCommandHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, command: UserCommand):
        stmt = (
            select(UserModel)
            .where(UserModel.userlogin == command.userlogin)
        )
        existing = await session.execute(stmt)
        if existing.unique().scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f'User with login {command.userlogin} already exists!')

        command.userpassword = cls.__hash_password(command.userpassword)

        model = UserModel(**command.model_dump())
        session.add(model)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return model


    @classmethod
    def __hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)



