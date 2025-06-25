"""fix movie-linked tables

Revision ID: 5cf2387759ac
Revises: 3de212ca7a72
Create Date: 2025-06-25 20:24:50.743836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cf2387759ac'
down_revision: Union[str, None] = '3de212ca7a72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop and recreate foreign keys with ON DELETE CASCADE
    op.drop_constraint('movie_cast_movieid_fkey', 'movie_cast', type_='foreignkey')
    op.create_foreign_key(
        'movie_cast_movieid_fkey',
        'movie_cast', 'movie',
        ['movieid'], ['movieid'],
        ondelete='CASCADE'
    )

    op.drop_constraint('movie_name_movieid_fkey', 'movie_name', type_='foreignkey')
    op.create_foreign_key(
        'movie_name_movieid_fkey',
        'movie_name', 'movie',
        ['movieid'], ['movieid'],
        ondelete='CASCADE'
    )

    op.drop_constraint('movie_countries_movieid_fkey', 'movie_countries', type_='foreignkey')
    op.create_foreign_key(
        'movie_countries_movieid_fkey',
        'movie_countries', 'movie',
        ['movieid'], ['movieid'],
        ondelete='CASCADE'
    )

    op.drop_constraint('movie_genres_movieid_fkey', 'movie_genres', type_='foreignkey')
    op.create_foreign_key(
        'movie_genres_movieid_fkey',
        'movie_genres', 'movie',
        ['movieid'], ['movieid'],
        ondelete='CASCADE'
    )


def downgrade():
    # Revert to no ON DELETE CASCADE
    op.drop_constraint('movie_cast_movieid_fkey', 'movie_cast', type_='foreignkey')
    op.create_foreign_key(
        'movie_cast_movieid_fkey',
        'movie_cast', 'movie',
        ['movieid'], ['movieid']
    )

    op.drop_constraint('movie_name_movieid_fkey', 'movie_name', type_='foreignkey')
    op.create_foreign_key(
        'movie_name_movieid_fkey',
        'movie_name', 'movie',
        ['movieid'], ['movieid']
    )

    op.drop_constraint('movie_countries_movieid_fkey', 'movie_countries', type_='foreignkey')
    op.create_foreign_key(
        'movie_countries_movieid_fkey',
        'movie_countries', 'movie',
        ['movieid'], ['movieid']
    )

    op.drop_constraint('movie_genres_movieid_fkey', 'movie_genres', type_='foreignkey')
    op.create_foreign_key(
        'movie_genres_movieid_fkey',
        'movie_genres', 'movie',
        ['movieid'], ['movieid']
    )