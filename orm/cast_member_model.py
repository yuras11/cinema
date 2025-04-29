import datetime
from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List

from orm.country_model import CountryModel


class PositionModel(Base):
    __tablename__ = "positions"

    positionid: Mapped[str] = mapped_column(primary_key=True)

    names: Mapped[List["PositionNameModel"]] = relationship(
        back_populates="position", cascade="all, delete-orphan"
    )

    cast_members: Mapped[List["CastMembersPositionsModel"]] = relationship(
        back_populates="positions", cascade="all, delete-orphan"
    )


class PositionNameModel(Base):
    __tablename__ = "positions_names"
    __table_args__ = (PrimaryKeyConstraint('positionid', 'languagecode'),)

    positionid: Mapped[str] = mapped_column(ForeignKey(PositionModel.positionid))
    languagecode: Mapped[str] = mapped_column(String(2))
    positionname: Mapped[str] = mapped_column(String(50))

    position: Mapped["PositionModel"] = relationship(back_populates="names")


class CastMemberModel(Base):
    __tablename__ = "cast_member"

    memberid: Mapped[str] = mapped_column(primary_key=True)
    dateofbirth: Mapped[datetime.date] = mapped_column(Date)
    countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))

    country: Mapped["CountryModel"] = relationship(back_populates="cast_members", lazy='subquery')

    names: Mapped[List["CastMemberNameModel"]] = relationship(
        back_populates="cast_member", cascade="all, delete-orphan", lazy='subquery'
    )

    positions: Mapped[List["CastMembersPositionsModel"]] = relationship(back_populates="cast_members")
    movies: Mapped[List["MovieCastModel"]] = relationship(back_populates="cast_members")


class CastMemberNameModel(Base):
    __tablename__ = "cast_member_names"
    __table_args__ = (PrimaryKeyConstraint('memberid', 'languagecode'),)

    memberid: Mapped[str] = mapped_column(ForeignKey(CastMemberModel.memberid))
    languagecode: Mapped[str] = mapped_column(String(2))
    membername: Mapped[str] = mapped_column(String(100))

    cast_member: Mapped["CastMemberModel"] = relationship(back_populates="names")


class CastMembersPositionsModel(Base):
    __tablename__ = "cast_members_positions"
    __table_args__ = (PrimaryKeyConstraint('memberid', 'positionid'),)

    memberid: Mapped[str] = mapped_column(ForeignKey(CastMemberModel.memberid))
    positionid: Mapped[str] = mapped_column(ForeignKey(PositionModel.positionid))

    cast_members: Mapped[List["CastMemberModel"]] = relationship(back_populates="positions")

    positions: Mapped[List["PositionModel"]] = relationship(back_populates="cast_members")