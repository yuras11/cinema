from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List
from datetime import timedelta, date
from sqlalchemy import Interval

from orm.cast_member_model import CastMemberModel
from orm.country_model import CountryModel


class GenreModel(Base):
    __tablename__ = "genre"

    genreid: Mapped[str] = mapped_column(primary_key=True)

    names: Mapped[List["GenreNameModel"]] = relationship(
        back_populates="genre", cascade="all, delete-orphan"
    )

    movies: Mapped[List["MovieGenreModel"]] = relationship(back_populates="genres")


class GenreNameModel(Base):
    __tablename__ = "genre_names"
    __table_args__ = (PrimaryKeyConstraint('genreid', 'languagecode'),)

    genreid: Mapped[str] = mapped_column(ForeignKey(GenreModel.genreid))
    languagecode: Mapped[str] = mapped_column(String(2))
    genrename: Mapped[str] = mapped_column(String(50))

    genre: Mapped["GenreModel"] = relationship(back_populates="names")


class MovieModel(Base):
    __tablename__ = "movie"

    movieid: Mapped[str] = mapped_column(primary_key=True)
    durationtime: Mapped[timedelta] = mapped_column(Interval)
    releasedate: Mapped[date] = mapped_column(Date)
    agerate: Mapped[str] = mapped_column(String(3))

    names: Mapped[List["MovieNameModel"]] = relationship(
        back_populates="movie", cascade="all, delete-orphan", lazy='subquery'
    )

    genres: Mapped[List["MovieGenreModel"]] = relationship(back_populates="movies", lazy='subquery')
    countries: Mapped[List["MovieCountryModel"]] = relationship(back_populates="movies", lazy='subquery')
    cast_members: Mapped[List["MovieCastModel"]] = relationship(back_populates="movies", lazy='subquery')
    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="movie", cascade="all, delete-orphan", lazy='subquery'
    )


class MovieNameModel(Base):
    __tablename__ = "movie_name"
    __table_args__ = (PrimaryKeyConstraint('movieid', 'languagecode'),)

    movieid: Mapped[str] = mapped_column(ForeignKey(MovieModel.movieid))
    languagecode: Mapped[str] = mapped_column(String(2))
    moviename: Mapped[str] = mapped_column(String(50))

    movie: Mapped["MovieModel"] = relationship(back_populates="names")


class MovieGenreModel(Base):
    __tablename__ = "movie_genres"
    __table_args__ = (PrimaryKeyConstraint('movieid', 'genreid'),)

    movieid: Mapped[str] = mapped_column(ForeignKey(MovieModel.movieid))
    genreid: Mapped[str] = mapped_column(ForeignKey(GenreModel.genreid))

    movies: Mapped[List["MovieModel"]] = relationship(back_populates="genres")
    genres: Mapped[List["GenreModel"]] = relationship(back_populates="movies")


class MovieCountryModel(Base):
    __tablename__ = "movie_countries"
    __table_args__ = (PrimaryKeyConstraint('movieid', 'countrycode'),)

    movieid: Mapped[str] = mapped_column(ForeignKey(MovieModel.movieid))
    countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))

    movies: Mapped[List["MovieModel"]] = relationship(back_populates="countries")
    countries: Mapped[List["CountryModel"]] = relationship(back_populates="movies")


class MovieCastModel(Base):
    __tablename__ = "movie_cast"
    __table_args__ = (PrimaryKeyConstraint('movieid', 'memberid'),)

    movieid: Mapped[str] = mapped_column(ForeignKey(MovieModel.movieid))
    memberid: Mapped[str] = mapped_column(ForeignKey(CastMemberModel.memberid))

    movies: Mapped[List["MovieModel"]] = relationship(back_populates="cast_members")
    cast_members: Mapped[List["CastMemberModel"]] = relationship(back_populates="movies")