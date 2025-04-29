from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List


class HallModel(Base):
    __tablename__ = "hall"

    hallid: Mapped[str] = mapped_column(primary_key=True)

    names: Mapped[List["HallNameModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='subquery'
    )
    seats: Mapped[List["SeatModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='subquery'
    )
    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='subquery'
    )

class HallNameModel(Base):
    __tablename__ = "hall_names"
    __table_args__ = (PrimaryKeyConstraint('hallid', 'languagecode'),)

    hallid: Mapped[str] = mapped_column(ForeignKey(HallModel.hallid))
    languagecode: Mapped[str] = mapped_column(String(2))
    hallname: Mapped[str] = mapped_column(String(50))

    hall: Mapped["HallModel"] = relationship(back_populates="names")


class SeatModel(Base):
    __tablename__ = "seat"
    __table_args__ = (PrimaryKeyConstraint('hallid', 'rownumber', 'seatnumber'),)

    hallid: Mapped[str] = mapped_column(ForeignKey(HallModel.hallid))
    rownumber: Mapped[int] = mapped_column(Integer)
    seatnumber: Mapped[int] = mapped_column(Integer)
    isoccupied: Mapped[bool] = mapped_column(Boolean)

    hall: Mapped["HallModel"] = relationship(back_populates="seats")