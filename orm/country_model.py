from sqlalchemy import String, ForeignKey, PrimaryKeyConstraint
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List


class CountryModel(Base):
    __tablename__ = "country"

    countrycode: Mapped[str] = mapped_column(primary_key=True)
    countryname: Mapped[str] = mapped_column(String(50))

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        back_populates="country", cascade="all, delete-orphan"
    )

    movies: Mapped[List["MovieModel"]] = relationship(
        secondary="movie_countries",
        back_populates="countries",
        lazy='joined'
    )