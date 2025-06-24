"""fix cast_members_positions_again

Revision ID: cc7082f53875
Revises: 9600faa50053
Create Date: 2025-06-24 22:26:55.567592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc7082f53875'
down_revision: Union[str, None] = '9600faa50053'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_constraint("cast_members_positions_memberid_fkey", "cast_members_positions", type_="foreignkey")
    op.create_foreign_key(
        "cast_members_positions_memberid_fkey",
        "cast_members_positions", "cast_member",
        ["memberid"], ["memberid"],
        ondelete="CASCADE"
    )

def downgrade():
    op.drop_constraint("cast_members_positions_memberid_fkey", "cast_members_positions", type_="foreignkey")
    op.create_foreign_key(
        "cast_members_positions_memberid_fkey",
        "cast_members_positions", "cast_member",
        ["memberid"], ["memberid"]
    )
