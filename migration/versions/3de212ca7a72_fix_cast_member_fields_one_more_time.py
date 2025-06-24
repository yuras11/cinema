"""fix cast_member fields one more time

Revision ID: 3de212ca7a72
Revises: cc7082f53875
Create Date: 2025-06-24 22:29:19.856971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3de212ca7a72'
down_revision: Union[str, None] = 'cc7082f53875'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удаляем старые внешние ключи
    op.drop_constraint("cast_member_names_memberid_fkey", "cast_member_names", type_="foreignkey")
    op.drop_constraint("movie_cast_memberid_fkey", "movie_cast", type_="foreignkey")
    op.drop_constraint("cast_members_positions_memberid_fkey", "cast_members_positions", type_="foreignkey")

    # Добавляем заново с ON DELETE CASCADE
    op.create_foreign_key(
        "cast_member_names_memberid_fkey",
        "cast_member_names", "cast_member",
        ["memberid"], ["memberid"],
        ondelete="CASCADE"
    )
    op.create_foreign_key(
        "cast_members_positions_memberid_fkey",
        "cast_members_positions", "cast_member",
        ["memberid"], ["memberid"],
        ondelete="CASCADE"
    )
    op.create_foreign_key(
        "movie_cast_memberid_fkey",
        "movie_cast", "cast_member",
        ["memberid"], ["memberid"],
        ondelete="CASCADE"
    )



def downgrade():
    # Удаляем каскадные ограничения
    op.drop_constraint("cast_member_names_memberid_fkey", "cast_member_names", type_="foreignkey")
    op.drop_constraint("movie_cast_memberid_fkey", "movie_cast", type_="foreignkey")
    op.drop_constraint("cast_members_positions_memberid_fkey", "cast_members_positions", type_="foreignkey")

    # Восстанавливаем без каскада
    op.create_foreign_key(
        "cast_member_names_memberid_fkey",
        "cast_member_names", "cast_member",
        ["memberid"], ["memberid"]
    )
    op.create_foreign_key(
        "movie_cast_memberid_fkey",
        "movie_cast", "cast_member",
        ["memberid"], ["memberid"]
    )
    op.create_foreign_key(
        "cast_members_positions_memberid_fkey",
        "cast_members_positions", "cast_member",
        ["memberid"], ["memberid"]
    )
