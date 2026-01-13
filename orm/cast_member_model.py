import datetime

from sqlalchemy import String, ForeignKey, Date
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List

from orm.country_model import CountryModel


class ProfessionModel(Base):
    __tablename__ = "profession"

    professionid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    professionname: Mapped[str] = mapped_column(String(50))

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        back_populates="profession",
        lazy='joined'
    )


class CastMemberModel(Base):
    __tablename__ = "cast_member"

    memberid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    membername: Mapped[str] = mapped_column(String(100))
    dateofbirth: Mapped[datetime.date] = mapped_column(Date)
    countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))
    professionid: Mapped[int] = mapped_column(ForeignKey(ProfessionModel.professionid))

    country: Mapped["CountryModel"] = relationship(
        back_populates="cast_members",
        lazy='selectin'
    )

    profession: Mapped[ProfessionModel] = relationship(
        back_populates="cast_members",
        lazy='selectin'
    )

    movies: Mapped[List["MovieModel"]] = relationship(
        secondary="movie_cast",
        back_populates="cast_members",
        lazy='selectin'
    )
