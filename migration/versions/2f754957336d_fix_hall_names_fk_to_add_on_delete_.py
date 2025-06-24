"""Fix hall_names FK to add ON DELETE CASCADE

Revision ID: 2f754957336d
Revises: c1ed4ca1e5bb
Create Date: 2025-06-10 16:01:32.725180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f754957336d'
down_revision: Union[str, None] = 'c1ed4ca1e5bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удаляем старый внешний ключ
    op.drop_constraint('hall_names_hallid_fkey', 'hall_names', type_='foreignkey')

    # Создаем новый с каскадом
    op.create_foreign_key(
        'hall_names_hallid_fkey',     # имя ограничения
        source_table='hall_names',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid'],
        ondelete='CASCADE'
    )


def downgrade():
    op.drop_constraint('hall_names_hallid_fkey', 'hall_names', type_='foreignkey')
    op.create_foreign_key(
        'hall_names_hallid_fkey',
        source_table='hall_names',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid']
        # Без CASCADE
    )
