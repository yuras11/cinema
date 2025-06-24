"""Fix FK for seat and cinema_session (add ON DELETE CASCADE)

Revision ID: 7566f3b9e127
Revises: 2f754957336d
Create Date: 2025-06-10 16:04:04.923991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7566f3b9e127'
down_revision: Union[str, None] = '2f754957336d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удалить старые ограничения
    op.drop_constraint('seat_hallid_fkey', 'seat', type_='foreignkey')
    op.drop_constraint('cinema_session_hallid_fkey', 'cinema_session', type_='foreignkey')

    # Добавить новые с ON DELETE CASCADE
    op.create_foreign_key(
        'seat_hallid_fkey',
        source_table='seat',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid'],
        ondelete='CASCADE'
    )

    op.create_foreign_key(
        'cinema_session_hallid_fkey',
        source_table='cinema_session',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid'],
        ondelete='CASCADE'
    )


def downgrade():
    # Удалить каскадные ограничения
    op.drop_constraint('seat_hallid_fkey', 'seat', type_='foreignkey')
    op.drop_constraint('cinema_session_hallid_fkey', 'cinema_session', type_='foreignkey')

    # Восстановить обычные (без CASCADE)
    op.create_foreign_key(
        'seat_hallid_fkey',
        source_table='seat',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid']
    )

    op.create_foreign_key(
        'cinema_session_hallid_fkey',
        source_table='cinema_session',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid']
    )
