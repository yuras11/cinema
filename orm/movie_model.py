from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date, Table, Column
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
    Column("movieid", ForeignKey("movie.movieid"), primary_key=True),
    Column("genreid", ForeignKey("genre.genreid"), primary_key=True)
)

movie_countries = Table(
    "movie_countries",
    Base.metadata,
    Column("movieid", ForeignKey("movie.movieid"), primary_key=True),
    Column("countrycode", ForeignKey("country.countrycode"), primary_key=True)
)

movie_cast = Table(
    "movie_cast",
    Base.metadata,
    Column("movieid", ForeignKey("movie.movieid"), primary_key=True),
    Column("memberid", ForeignKey("cast_member.memberid"), primary_key=True),
)


class GenreModel(Base):
    __tablename__ = "genre"

    genreid: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    names: Mapped[List["GenreNameModel"]] = relationship(
        back_populates="genre",
        cascade="all, delete-orphan"
    )

    movies: Mapped[List["MovieModel"]] = relationship(
        secondary=movie_genres,
        back_populates="genres",
        lazy='joined'
    )


class GenreNameModel(Base):
    __tablename__ = "genre_names"
    __table_args__ = (PrimaryKeyConstraint('genreid', 'languagecode'),)

    genreid: Mapped[uuid.UUID] = mapped_column(ForeignKey(GenreModel.genreid))
    languagecode: Mapped[str] = mapped_column(String(2))
    genrename: Mapped[str] = mapped_column(String(50))

    genre: Mapped["GenreModel"] = relationship(back_populates="names")


class MovieModel(Base):
    __tablename__ = "movie"

    movieid: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    durationtime: Mapped[timedelta] = mapped_column(Interval)
    releasedate: Mapped[date] = mapped_column(Date)
    agerate: Mapped[str] = mapped_column(String(3))

    names: Mapped[List["MovieNameModel"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
        lazy='joined'
    )

    genres: Mapped[List["GenreModel"]] = relationship(
        secondary=movie_genres,
        back_populates="movies",
        lazy='joined'
    )

    countries: Mapped[List["CountryModel"]] = relationship(
        secondary=movie_countries,
        back_populates="movies",
        lazy='joined'
    )

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        secondary=movie_cast,
        back_populates="movies",
        lazy="joined"
    )

    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="movie", cascade="all, delete-orphan", lazy='subquery'
    )


class MovieNameModel(Base):
    __tablename__ = "movie_name"
    __table_args__ = (PrimaryKeyConstraint('movieid', 'languagecode'),)

    movieid: Mapped[uuid.UUID] = mapped_column(ForeignKey(MovieModel.movieid))
    languagecode: Mapped[str] = mapped_column(String(2))
    moviename: Mapped[str] = mapped_column(String(50))

    movie: Mapped["MovieModel"] = relationship(back_populates="names")


# class MovieCountryModel(Base):
#     __tablename__ = "movie_countries"
#     __table_args__ = (PrimaryKeyConstraint('movieid', 'countrycode'),)
#
#     movieid: Mapped[uuid.UUID] = mapped_column(ForeignKey(MovieModel.movieid))
#     countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))
#
#     movies: Mapped[List["MovieModel"]] = relationship(back_populates="countries")
#     countries: Mapped[List["CountryModel"]] = relationship(back_populates="movies")
#
#
# class MovieCastModel(Base):
#     __tablename__ = "movie_cast"
#     __table_args__ = (PrimaryKeyConstraint('movieid', 'memberid'),)
#
#     movieid: Mapped[uuid.UUID] = mapped_column(ForeignKey(MovieModel.movieid))
#     memberid: Mapped[uuid.UUID] = mapped_column(ForeignKey(CastMemberModel.memberid))
#
#     movies: Mapped[List["MovieModel"]] = relationship(back_populates="cast_members")
#     cast_members: Mapped[List["CastMemberModel"]] = relationship(back_populates="movies")


# class MovieGenreModel(Base):
#     __tablename__ = "movie_genres"
#     __table_args__ = (PrimaryKeyConstraint('movieid', 'genreid'),)
#
#     movieid: Mapped[uuid.UUID] = mapped_column(ForeignKey(MovieModel.movieid))
#     genreid: Mapped[uuid.UUID] = mapped_column(ForeignKey(GenreModel.genreid))
#
#     movies: Mapped[List["MovieModel"]] = relationship(back_populates="genres")
#     genres: Mapped[List["GenreModel"]] = relationship(back_populates="movies")