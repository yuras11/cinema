from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date, Table, Column, Text
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List
from datetime import timedelta, date
from sqlalchemy import Interval

from orm.cast_member_model import CastMemberModel
from orm.country_model import CountryModel
import uuid


movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column("movieid", ForeignKey("movie.movieid", ondelete="CASCADE"), primary_key=True),
    Column("genreid", ForeignKey("genre.genreid"), primary_key=True)
)

movie_countries = Table(
    "movie_countries",
    Base.metadata,
    Column("movieid", ForeignKey("movie.movieid", ondelete="CASCADE"), primary_key=True),
    Column("countrycode", ForeignKey("country.countrycode"), primary_key=True)
)

movie_cast = Table(
    "movie_cast",
    Base.metadata,
    Column("movieid", ForeignKey("movie.movieid", ondelete="CASCADE"), primary_key=True),
    Column("memberid", ForeignKey("cast_member.memberid"), primary_key=True),
)


class GenreModel(Base):
    __tablename__ = "genre"

    genreid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    genrename: Mapped[str] = mapped_column(String(50))

    movies: Mapped[List["MovieModel"]] = relationship(
        secondary=movie_genres,
        back_populates="genres",
        lazy='joined'
    )


class MovieModel(Base):
    __tablename__ = "movie"

    movieid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    moviename: Mapped[str] = mapped_column(String(100))
    durationtime: Mapped[timedelta] = mapped_column(Interval)
    releaseyear: Mapped[int] = mapped_column(Integer)
    agerate: Mapped[str] = mapped_column(String(3))
    moviephoto: Mapped[str] = mapped_column(Text, nullable=True)


    genres: Mapped[List["GenreModel"]] = relationship(
        secondary=movie_genres,
        back_populates="movies",
#        lazy='joined',
        passive_deletes=True
    )

    countries: Mapped[List["CountryModel"]] = relationship(
        secondary=movie_countries,
        back_populates="movies",
#        lazy='joined',
        passive_deletes=True
    )

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        secondary=movie_cast,
        back_populates="movies",
        lazy="joined",
        passive_deletes=True
    )

    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
        lazy='selectin'
    )
