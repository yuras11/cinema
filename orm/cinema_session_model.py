from sqlalchemy import String, PrimaryKeyConstraint, Boolean, Integer, ForeignKey, Date, Numeric
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List
from datetime import timedelta, date
from sqlalchemy import Interval

from orm.hall_model import HallModel
from orm.movie_model import MovieModel
import uuid


class CinemaSessionModel(Base):
    __tablename__ = "cinema_session"
    __table_args__ = (PrimaryKeyConstraint("movieid", "hallid", "sessiondate", "sessiontime"),)

    movieid: Mapped[uuid.UUID] = mapped_column(ForeignKey(MovieModel.movieid))
    hallid: Mapped[uuid.UUID] = mapped_column(ForeignKey(HallModel.hallid, ondelete='CASCADE'))
    sessiondate: Mapped[date] = mapped_column(Date)
    sessiontime: Mapped[timedelta] = mapped_column(Interval)
    ticketfee: Mapped[float] = mapped_column(Numeric)
    currencycode: Mapped[str] = mapped_column(String(3))

    movie: Mapped["MovieModel"] = relationship(back_populates="cinema_sessions", lazy='joined')
    hall: Mapped["HallModel"] = relationship(back_populates="cinema_sessions", lazy='joined')

    seat_statuses: Mapped[List["SeatStatusModel"]] = relationship(
        "SeatStatusModel", back_populates="cinema_session",
        cascade="all, delete-orphan", passive_deletes=True,
        overlaps="seat,seat_statuses"
    )