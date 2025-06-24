"""Increase password length to 70

Revision ID: 00188467dfb9
Revises: 7566f3b9e127
Create Date: 2025-06-17 20:43:38.155034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00188467dfb9'
down_revision: Union[str, None] = '7566f3b9e127'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        'cinema_user',
        'userpassword',
        existing_type=sa.String(length=50),  # замените на текущее значение, если отличается
        type_=sa.String(length=70),
        existing_nullable=False
    )


def downgrade():
    op.alter_column(
        'cinema_user',
        'userpassword',
        existing_type=sa.String(length=70),
        type_=sa.String(length=50),  # замените на старое значение
        existing_nullable=False
    )
