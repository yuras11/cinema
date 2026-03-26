from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from orm.user_model import UserModel
from api.comands.user.user_command import UserCommand
from database import connection


class UpdateUserCommandHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    @connection
    async def handle_async(cls, session: AsyncSession, userid: str, command: UserCommand):
        stmt = (
            select(UserModel)
            .where(UserModel.userid == userid)
        )
        existing = await session.execute(stmt)
        user = existing.unique().scalar_one_or_none()

        if user is None:
            return None

        user.userlogin = command.userlogin
        user.userpassword = cls.__hash_password(command.userpassword)
        user.username = command.username
        user.useremail = command.useremail

        try:
            await session.commit()
            await session.refresh(user)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return user


    @classmethod
    def __hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)
