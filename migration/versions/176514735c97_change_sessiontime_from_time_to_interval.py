"""Change sessiontime from time to interval

Revision ID: 176514735c97
Revises: 5cf2387759ac
Create Date: 2025-06-25 22:21:28.004765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '176514735c97'
down_revision: Union[str, None] = '5cf2387759ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("seat_status") as batch_op:
        batch_op.alter_column(
            "sessiontime",
            type_=sa.Interval(),
            existing_type=sa.Time(),
            postgresql_using="sessiontime::interval"
        )

def downgrade():
    with op.batch_alter_table("seat_status") as batch_op:
        batch_op.alter_column(
            "sessiontime",
            type_=sa.Time(),
            existing_type=sa.Interval(),
            postgresql_using="sessiontime::time"
        )
