from orm.base_model import Base
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid


class UserModel(Base):
    __tablename__ = "cinema_user"

    userid: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    userlogin: Mapped[str] = mapped_column(String(50))
    userpassword: Mapped[str] = mapped_column(String(70))
    username: Mapped[str] = mapped_column(String(50))
    usersurname: Mapped[str] = mapped_column(String(50))
    userrole: Mapped[bool] = mapped_column(Boolean)