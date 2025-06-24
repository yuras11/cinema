from sqlalchemy import String, ForeignKey, PrimaryKeyConstraint
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List


class CountryModel(Base):
    __tablename__ = "country"

    countrycode: Mapped[str] = mapped_column(primary_key=True)

    names: Mapped[List["CountryNameModel"]] = relationship(
        back_populates="country", cascade="all, delete-orphan", lazy='joined'
    )

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        back_populates="country", cascade="all, delete-orphan"
    )
    movies: Mapped[List["MovieModel"]] = relationship(
        secondary="movie_countries",
        back_populates="countries",
        lazy='joined'
    )


class CountryNameModel(Base):
    __tablename__ = "country_names"
    __table_args__ = (PrimaryKeyConstraint('countrycode', 'languagecode'),)

    countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))
    languagecode: Mapped[str] = mapped_column(String(2))
    countryname: Mapped[str] = mapped_column(String(50))

    country: Mapped["CountryModel"] = relationship(back_populates="names")