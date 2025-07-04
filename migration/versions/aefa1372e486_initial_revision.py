"""Initial revision

Revision ID: aefa1372e486
Revises: 
Create Date: 2025-05-02 19:19:51.578425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aefa1372e486'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cast_member', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.alter_column('cast_member', 'countrycode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_constraint('cast_member_countrycode_fkey', 'cast_member', type_='foreignkey')
    op.create_foreign_key(None, 'cast_member', 'country', ['countrycode'], ['countrycode'])
    op.alter_column('cast_member_names', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cast_member_names', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('cast_member_names', 'membername',
               existing_type=sa.CHAR(length=100),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.drop_constraint('cast_member_names_memberid_fkey', 'cast_member_names', type_='foreignkey')
    op.create_foreign_key(None, 'cast_member_names', 'cast_member', ['memberid'], ['memberid'])
    op.alter_column('cast_members_positions', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cast_members_positions', 'positionid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint('cast_members_positions_positionid_fkey', 'cast_members_positions', type_='foreignkey')
    op.drop_constraint('cast_members_positions_memberid_fkey', 'cast_members_positions', type_='foreignkey')
    op.create_foreign_key(None, 'cast_members_positions', 'cast_member', ['memberid'], ['memberid'])
    op.create_foreign_key(None, 'cast_members_positions', 'positions', ['positionid'], ['positionid'])
    op.alter_column('cinema_session', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cinema_session', 'hallid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cinema_session', 'currencycode',
               existing_type=sa.CHAR(length=3),
               type_=sa.String(length=3),
               existing_nullable=False)
    op.drop_constraint('cinema_session_movieid_fkey', 'cinema_session', type_='foreignkey')
    op.drop_constraint('cinema_session_hallid_fkey', 'cinema_session', type_='foreignkey')
    op.create_foreign_key(None, 'cinema_session', 'movie', ['movieid'], ['movieid'])
    op.create_foreign_key(None, 'cinema_session', 'hall', ['hallid'], ['hallid'])
    op.alter_column('cinema_user', 'userid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.alter_column('cinema_user', 'userlogin',
               existing_type=sa.CHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('cinema_user', 'userpassword',
               existing_type=sa.CHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('cinema_user', 'username',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('cinema_user', 'usersurname',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('country', 'countrycode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('country_names', 'countrycode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('country_names', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('country_names', 'countryname',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.drop_constraint('country_names_countrycode_fkey', 'country_names', type_='foreignkey')
    op.create_foreign_key(None, 'country_names', 'country', ['countrycode'], ['countrycode'])
    op.alter_column('genre', 'genreid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.alter_column('genre_names', 'genreid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('genre_names', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('genre_names', 'genrename',
               existing_type=sa.CHAR(length=50),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.drop_constraint('genre_names_genreid_fkey', 'genre_names', type_='foreignkey')
    op.create_foreign_key(None, 'genre_names', 'genre', ['genreid'], ['genreid'])
    op.alter_column('hall', 'hallid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_column('hall', 'capacity')
    op.alter_column('hall_names', 'hallid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('hall_names', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('hall_names', 'hallname',
               existing_type=sa.CHAR(length=50),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.drop_constraint('hall_names_hallid_fkey', 'hall_names', type_='foreignkey')
    op.create_foreign_key(
        'hall_names_hallid_fkey',
        source_table='hall_names',
        referent_table='hall',
        local_cols=['hallid'],
        remote_cols=['hallid'],
        ondelete='CASCADE'
    )
    #op.create_foreign_key(None, 'hall_names', 'hall', ['hallid'], ['hallid'])
    op.alter_column('movie', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.alter_column('movie', 'agerate',
               existing_type=sa.CHAR(length=3),
               type_=sa.String(length=3),
               existing_nullable=False)
    op.alter_column('movie_cast', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_cast', 'memberid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint('movie_cast_memberid_fkey', 'movie_cast', type_='foreignkey')
    op.drop_constraint('movie_cast_movieid_fkey', 'movie_cast', type_='foreignkey')
    op.create_foreign_key(None, 'movie_cast', 'cast_member', ['memberid'], ['memberid'])
    op.create_foreign_key(None, 'movie_cast', 'movie', ['movieid'], ['movieid'])
    op.alter_column('movie_countries', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_countries', 'countrycode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_constraint('movie_countries_countrycode_fkey', 'movie_countries', type_='foreignkey')
    op.drop_constraint('movie_countries_movieid_fkey', 'movie_countries', type_='foreignkey')
    op.create_foreign_key(None, 'movie_countries', 'movie', ['movieid'], ['movieid'])
    op.create_foreign_key(None, 'movie_countries', 'country', ['countrycode'], ['countrycode'])
    op.alter_column('movie_genres', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_genres', 'genreid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint('movie_genres_genreid_fkey', 'movie_genres', type_='foreignkey')
    op.drop_constraint('movie_genres_movieid_fkey', 'movie_genres', type_='foreignkey')
    op.create_foreign_key(None, 'movie_genres', 'movie', ['movieid'], ['movieid'])
    op.create_foreign_key(None, 'movie_genres', 'genre', ['genreid'], ['genreid'])
    op.alter_column('movie_name', 'movieid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_name', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('movie_name', 'moviename',
               existing_type=sa.CHAR(length=50),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.drop_constraint('movie_name_movieid_fkey', 'movie_name', type_='foreignkey')
    op.create_foreign_key(None, 'movie_name', 'movie', ['movieid'], ['movieid'])
    op.alter_column('positions', 'positionid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.alter_column('positions_names', 'positionid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('positions_names', 'languagecode',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               existing_nullable=False)
    op.alter_column('positions_names', 'positionname',
               existing_type=sa.CHAR(length=50),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.drop_constraint('positions_names_positionid_fkey', 'positions_names', type_='foreignkey')
    op.create_foreign_key(None, 'positions_names', 'positions', ['positionid'], ['positionid'])
    op.alter_column('seat', 'hallid',
               existing_type=sa.UUID(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint('seat_hallid_fkey', 'seat', type_='foreignkey')
    op.create_foreign_key(None, 'seat', 'hall', ['hallid'], ['hallid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'seat', type_='foreignkey')
    op.create_foreign_key('seat_hallid_fkey', 'seat', 'hall', ['hallid'], ['hallid'], ondelete='CASCADE')
    op.alter_column('seat', 'hallid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'positions_names', type_='foreignkey')
    op.create_foreign_key('positions_names_positionid_fkey', 'positions_names', 'positions', ['positionid'], ['positionid'], ondelete='CASCADE')
    op.alter_column('positions_names', 'positionname',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=50),
               existing_nullable=False)
    op.alter_column('positions_names', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('positions_names', 'positionid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('positions', 'positionid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_constraint(None, 'movie_name', type_='foreignkey')
    op.create_foreign_key('movie_name_movieid_fkey', 'movie_name', 'movie', ['movieid'], ['movieid'], ondelete='CASCADE')
    op.alter_column('movie_name', 'moviename',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=50),
               existing_nullable=False)
    op.alter_column('movie_name', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('movie_name', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'movie_genres', type_='foreignkey')
    op.drop_constraint(None, 'movie_genres', type_='foreignkey')
    op.create_foreign_key('movie_genres_movieid_fkey', 'movie_genres', 'movie', ['movieid'], ['movieid'], ondelete='CASCADE')
    op.create_foreign_key('movie_genres_genreid_fkey', 'movie_genres', 'genre', ['genreid'], ['genreid'], ondelete='CASCADE')
    op.alter_column('movie_genres', 'genreid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_genres', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'movie_countries', type_='foreignkey')
    op.drop_constraint(None, 'movie_countries', type_='foreignkey')
    op.create_foreign_key('movie_countries_movieid_fkey', 'movie_countries', 'movie', ['movieid'], ['movieid'], ondelete='CASCADE')
    op.create_foreign_key('movie_countries_countrycode_fkey', 'movie_countries', 'country', ['countrycode'], ['countrycode'], ondelete='CASCADE')
    op.alter_column('movie_countries', 'countrycode',
               existing_type=sa.String(),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('movie_countries', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'movie_cast', type_='foreignkey')
    op.drop_constraint(None, 'movie_cast', type_='foreignkey')
    op.create_foreign_key('movie_cast_movieid_fkey', 'movie_cast', 'movie', ['movieid'], ['movieid'], ondelete='CASCADE')
    op.create_foreign_key('movie_cast_memberid_fkey', 'movie_cast', 'cast_member', ['memberid'], ['memberid'], ondelete='CASCADE')
    op.alter_column('movie_cast', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie_cast', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('movie', 'agerate',
               existing_type=sa.String(length=3),
               type_=sa.CHAR(length=3),
               existing_nullable=False)
    op.alter_column('movie', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_constraint(None, 'hall_names', type_='foreignkey')
    op.create_foreign_key('hall_names_hallid_fkey', 'hall_names', 'hall', ['hallid'], ['hallid'], ondelete='CASCADE')
    op.alter_column('hall_names', 'hallname',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=50),
               existing_nullable=False)
    op.alter_column('hall_names', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('hall_names', 'hallid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.add_column('hall', sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('hall', 'hallid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_constraint(None, 'genre_names', type_='foreignkey')
    op.create_foreign_key('genre_names_genreid_fkey', 'genre_names', 'genre', ['genreid'], ['genreid'], ondelete='CASCADE')
    op.alter_column('genre_names', 'genrename',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=50),
               existing_nullable=False)
    op.alter_column('genre_names', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('genre_names', 'genreid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('genre', 'genreid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_constraint(None, 'country_names', type_='foreignkey')
    op.create_foreign_key('country_names_countrycode_fkey', 'country_names', 'country', ['countrycode'], ['countrycode'], ondelete='CASCADE')
    op.alter_column('country_names', 'countryname',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('country_names', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('country_names', 'countrycode',
               existing_type=sa.String(),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('country', 'countrycode',
               existing_type=sa.String(),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('cinema_user', 'usersurname',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('cinema_user', 'username',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('cinema_user', 'userpassword',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=30),
               existing_nullable=False)
    op.alter_column('cinema_user', 'userlogin',
               existing_type=sa.String(length=50),
               type_=sa.CHAR(length=30),
               existing_nullable=False)
    op.alter_column('cinema_user', 'userid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    op.drop_constraint(None, 'cinema_session', type_='foreignkey')
    op.drop_constraint(None, 'cinema_session', type_='foreignkey')
    op.create_foreign_key('cinema_session_hallid_fkey', 'cinema_session', 'hall', ['hallid'], ['hallid'], ondelete='CASCADE')
    op.create_foreign_key('cinema_session_movieid_fkey', 'cinema_session', 'movie', ['movieid'], ['movieid'], ondelete='CASCADE')
    op.alter_column('cinema_session', 'currencycode',
               existing_type=sa.String(length=3),
               type_=sa.CHAR(length=3),
               existing_nullable=False)
    op.alter_column('cinema_session', 'hallid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cinema_session', 'movieid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'cast_members_positions', type_='foreignkey')
    op.drop_constraint(None, 'cast_members_positions', type_='foreignkey')
    op.create_foreign_key('cast_members_positions_memberid_fkey', 'cast_members_positions', 'cast_member', ['memberid'], ['memberid'], ondelete='CASCADE')
    op.create_foreign_key('cast_members_positions_positionid_fkey', 'cast_members_positions', 'positions', ['positionid'], ['positionid'], ondelete='CASCADE')
    op.alter_column('cast_members_positions', 'positionid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('cast_members_positions', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'cast_member_names', type_='foreignkey')
    op.create_foreign_key('cast_member_names_memberid_fkey', 'cast_member_names', 'cast_member', ['memberid'], ['memberid'], ondelete='CASCADE')
    op.alter_column('cast_member_names', 'membername',
               existing_type=sa.String(length=100),
               type_=sa.CHAR(length=100),
               existing_nullable=False)
    op.alter_column('cast_member_names', 'languagecode',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('cast_member_names', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_constraint(None, 'cast_member', type_='foreignkey')
    op.create_foreign_key('cast_member_countrycode_fkey', 'cast_member', 'country', ['countrycode'], ['countrycode'], ondelete='CASCADE')
    op.alter_column('cast_member', 'countrycode',
               existing_type=sa.String(),
               type_=sa.CHAR(length=2),
               existing_nullable=False)
    op.alter_column('cast_member', 'memberid',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
    # ### end Alembic commands ###
