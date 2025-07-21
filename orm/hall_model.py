from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, ForeignKeyConstraint
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List
import uuid
import datetime


class HallModel(Base):
    __tablename__ = "hall"

    hallid: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    names: Mapped[List["HallNameModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='joined', passive_deletes=True
    )
    seats: Mapped[List["SeatModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='joined', passive_deletes=True
    )
    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='joined', passive_deletes=True
    )


class HallNameModel(Base):
    __tablename__ = "hall_names"
    __table_args__ = (PrimaryKeyConstraint('hallid', 'languagecode'),)

    hallid: Mapped[uuid.UUID] = mapped_column(ForeignKey(HallModel.hallid, ondelete='CASCADE'))
    languagecode: Mapped[str] = mapped_column(String(2))
    hallname: Mapped[str] = mapped_column(String(50))

    hall: Mapped["HallModel"] = relationship(back_populates="names")


class SeatModel(Base):
    __tablename__ = "seat"
    __table_args__ = (PrimaryKeyConstraint('hallid', 'rownumber', 'seatnumber'),)

    hallid: Mapped[uuid.UUID] = mapped_column(ForeignKey(HallModel.hallid, ondelete='CASCADE'))
    rownumber: Mapped[int] = mapped_column(Integer)
    seatnumber: Mapped[int] = mapped_column(Integer)

    hall: Mapped["HallModel"] = relationship(back_populates="seats")

    seat_statuses: Mapped[List["SeatStatusModel"]] = relationship(
        back_populates="seat", cascade="all, delete-orphan", passive_deletes=True
    )


class SeatStatusModel(Base):
    __tablename__ = "seat_status"
    __table_args__ = (
        PrimaryKeyConstraint("movieid", "hallid", "sessiondate", "sessiontime", "rownumber", "seatnumber"),
        ForeignKeyConstraint(
            ["hallid", "rownumber", "seatnumber"],
            ["seat.hallid", "seat.rownumber", "seat.seatnumber"],
            ondelete="CASCADE"
        ),
        ForeignKeyConstraint(
            ["movieid", "hallid", "sessiondate", "sessiontime"],
            ["cinema_session.movieid", "cinema_session.hallid", "cinema_session.sessiondate",
             "cinema_session.sessiontime"],
            ondelete="CASCADE"
        ),
        ForeignKeyConstraint(
            ["userid"], ["cinema_user.userid"],
            ondelete="SET NULL"
        )
    )

    movieid: Mapped[uuid.UUID]
    hallid: Mapped[uuid.UUID]
    sessiondate: Mapped[datetime.date]
    sessiontime: Mapped[datetime.timedelta]
    rownumber: Mapped[int]
    seatnumber: Mapped[int]
    isoccupied: Mapped[bool] = mapped_column(default=False)

    userid: Mapped[uuid.UUID] = mapped_column(nullable=True)

    seat: Mapped["SeatModel"] = relationship(back_populates="seat_statuses")

    cinema_session: Mapped["CinemaSessionModel"] = relationship(back_populates="seat_statuses")

    user: Mapped["UserModel"] = relationship(back_populates="seat_statuses", lazy="joined")