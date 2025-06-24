"""Refactor seat occupancy to session level

Revision ID: 3045cc9678e1
Revises: 00188467dfb9
Create Date: 2025-06-24 20:05:18.989553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3045cc9678e1'
down_revision: Union[str, None] = '00188467dfb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удаляем isoccupied из seat
    with op.batch_alter_table("seat") as batch_op:
        batch_op.drop_column("isoccupied")

    # Создаём таблицу seat_status
    op.create_table(
        "seat_status",
        sa.Column("movieid", sa.UUID(), nullable=False),
        sa.Column("hallid", sa.UUID(), nullable=False),
        sa.Column("sessiondate", sa.DATE(), nullable=False),
        sa.Column("sessiontime", sa.TIME(), nullable=False),
        sa.Column("rownumber", sa.Integer(), nullable=False),
        sa.Column("seatnumber", sa.Integer(), nullable=False),
        sa.Column("isoccupied", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.ForeignKeyConstraint(
            ["movieid", "hallid", "sessiondate", "sessiontime"],
            ["cinema_session.movieid", "cinema_session.hallid", "cinema_session.sessiondate", "cinema_session.sessiontime"],
            ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint(
            "movieid", "hallid", "sessiondate", "sessiontime", "rownumber", "seatnumber"
        )
    )


def downgrade():
    op.drop_table("seat_status")

    with op.batch_alter_table("seat") as batch_op:
        batch_op.add_column(sa.Column("isoccupied", sa.Boolean(), nullable=False, server_default=sa.text("false")))