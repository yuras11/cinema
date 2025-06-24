"""fix cast_members_positions

Revision ID: 9600faa50053
Revises: e63267fc50f8
Create Date: 2025-06-24 22:21:14.131403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9600faa50053'
down_revision: Union[str, None] = 'e63267fc50f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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
