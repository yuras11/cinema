import datetime
import uuid

from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date, column, Table
from sqlalchemy.testing.schema import Column
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List

from orm.country_model import CountryModel


cast_members_positions = Table(
    "cast_members_positions",
    Base.metadata,
    Column("memberid", ForeignKey("cast_member.memberid"), primary_key=True),
    Column("positionid", ForeignKey("positions.positionid"), primary_key=True)
)


class PositionModel(Base):
    __tablename__ = "positions"

    positionid: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    names: Mapped[List["PositionNameModel"]] = relationship(
        back_populates="position",
        cascade="all, delete-orphan",
        lazy='joined'
    )

    cast_members: Mapped[List["CastMemberModel"]] = relationship(
        secondary=cast_members_positions,
        back_populates="positions",
        lazy='joined'
    )


class PositionNameModel(Base):
    __tablename__ = "positions_names"
    __table_args__ = (PrimaryKeyConstraint('positionid', 'languagecode'),)

    positionid: Mapped[uuid.UUID] = mapped_column(ForeignKey(PositionModel.positionid))
    languagecode: Mapped[str] = mapped_column(String(2))
    positionname: Mapped[str] = mapped_column(String(50))

    position: Mapped["PositionModel"] = relationship(back_populates="names")


class CastMemberModel(Base):
    __tablename__ = "cast_member"

    memberid: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    dateofbirth: Mapped[datetime.date] = mapped_column(Date)
    countrycode: Mapped[str] = mapped_column(ForeignKey(CountryModel.countrycode))

    country: Mapped["CountryModel"] = relationship(
        back_populates="cast_members",
        lazy='joined'
    )

    names: Mapped[List["CastMemberNameModel"]] = relationship(
        back_populates="cast_member",
        cascade="all, delete-orphan",
        lazy='joined',
        passive_deletes=True
    )

    positions: Mapped[List["PositionModel"]] = relationship(
        secondary=cast_members_positions,
        back_populates="cast_members",
        lazy='joined'
    )

    movies: Mapped[List["MovieModel"]] = relationship(
        secondary="movie_cast",
        back_populates="cast_members",
        lazy='joined'
    )


class CastMemberNameModel(Base):
    __tablename__ = "cast_member_names"
    __table_args__ = (PrimaryKeyConstraint('memberid', 'languagecode'),)

    memberid: Mapped[uuid.UUID] = mapped_column(ForeignKey(CastMemberModel.memberid))
    languagecode: Mapped[str] = mapped_column(String(2))
    membername: Mapped[str] = mapped_column(String(100))

    cast_member: Mapped["CastMemberModel"] = relationship(back_populates="names")


# class CastMembersPositionsModel(Base):
#     __tablename__ = "cast_members_positions"
#     __table_args__ = (PrimaryKeyConstraint('memberid', 'positionid'),)
#
#     memberid: Mapped[uuid.UUID] = mapped_column(ForeignKey(CastMemberModel.memberid))
#     positionid: Mapped[uuid.UUID] = mapped_column(ForeignKey(PositionModel.positionid))
#
#     cast_members: Mapped[List["CastMemberModel"]] = relationship(back_populates="positions")
#
#     positions: Mapped[List["PositionModel"]] = relationship(back_populates="cast_members")