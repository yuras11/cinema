"""Add userid to seat_status

Revision ID: 3689af982d8f
Revises: 3045cc9678e1
Create Date: 2025-06-24 20:14:39.703151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3689af982d8f'
down_revision: Union[str, None] = '3045cc9678e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("seat_status", sa.Column("userid", sa.UUID(), nullable=True))
    op.create_foreign_key(
        "fk_seat_status_userid_user",
        "seat_status", "cinema_user",
        ["userid"], ["userid"]
    )


def downgrade():
    op.drop_constraint("fk_seat_status_userid_user", "seat_status", type_="foreignkey")
    op.drop_column("seat_status", "userid")