from sqlalchemy import String, PrimaryKeyConstraint, Integer, ForeignKey, ForeignKeyConstraint
from orm.base_model import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from typing import List
import uuid


class HallModel(Base):
    __tablename__ = "hall"

    hallid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hallname: Mapped[str] = mapped_column(String(50))
    rowamount: Mapped[int] = mapped_column(Integer)
    seatamount: Mapped[int] = mapped_column(Integer)

    seats: Mapped[List["SeatModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='joined', passive_deletes=True
    )

    cinema_sessions: Mapped[List["CinemaSessionModel"]] = relationship(
        back_populates="hall", cascade="all, delete-orphan", lazy='joined', passive_deletes=True
    )


class SeatModel(Base):
    __tablename__ = "seat"
    __table_args__ = (PrimaryKeyConstraint('hallid', 'rownumber', 'seatnumber'),)

    hallid: Mapped[int] = mapped_column(ForeignKey(HallModel.hallid, ondelete='CASCADE'))
    rownumber: Mapped[int] = mapped_column(Integer)
    seatnumber: Mapped[int] = mapped_column(Integer)

    hall: Mapped["HallModel"] = relationship(back_populates="seats")


class SeatStatusModel(Base):
    __tablename__ = "seat_status"
    __table_args__ = (
        PrimaryKeyConstraint(
            "sessionid", "rownumber", "seatnumber"
        ),
        ForeignKeyConstraint(
            ["userid"], ["cinema_user.userid"],
            ondelete="SET NULL"
        ),
        ForeignKeyConstraint(
            ["sessionid"], ["cinema_session.sessionid"],
            ondelete='CASCADE'
        )
    )

    sessionid: Mapped[int]
    hallid: Mapped[int]
    rownumber: Mapped[int]
    seatnumber: Mapped[int]
    userid: Mapped[uuid.UUID] = mapped_column(nullable=True)

    cinema_session: Mapped["CinemaSessionModel"] = relationship(back_populates="seat_statuses", lazy='joined')

    user: Mapped["UserModel"] = relationship(back_populates="seat_statuses")