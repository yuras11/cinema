from z_JUNK.repository_old.base_repository import BaseRepository
from z_JUNK.repository_old.country_repository import CountryRepository
from z_JUNK.repository_old.position_repository import PositionRepository
from z_JUNK.entity.cast_member import CastMember


lang = 'RU'

class CastMemberRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self.__country_dao = CountryRepository(connection)
        self.__position_dao = PositionRepository(connection)


    def __get_single_entry(self, cursor, member_id):
        cursor.execute(
            "SELECT dateOfBirth, countryCode FROM cast_member WHERE memberID = %s",
            (member_id,)
        )
        date_of_birth, country_code = cursor.fetchone()

        # getting name
        cursor.execute(
            "SELECT memberName FROM cast_member_names WHERE memberID = %s AND languageCode = %s",
            (member_id, lang)
        )
        member_name = cursor.fetchone()[0].strip()

        # getting country
        country = self.__country_dao.get(country_code, lang)

        # getting positions
        member_positions= self.__position_dao.get_by_cast_member(member_id)

        return CastMember(member_id, member_name, date_of_birth, country, member_positions)


    def get_all(self) -> list[CastMember]:
        with self._connection.cursor() as cursor:
            # get data from cast_member
            cast_members_list = []
            cursor.execute("SELECT memberID FROM cast_member")
            cast_member_ids = [row[0] for row in cursor.fetchall()]
            for member_id in cast_member_ids:
                cast_members_list.append(self.__get_single_entry(cursor, member_id))

            return cast_members_list


    def get_by_name(self, name: str) -> list[CastMember]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT memberID FROM cast_member_names WHERE memberName = %s",
                (name,)
            )
            member_ids = [row[0] for row in cursor.fetchall()]
            cast_members_list = []
            for member_id in member_ids:
                cast_members_list.append(self.__get_single_entry(cursor, member_id))
            return cast_members_list


    def get_by_movie(self, movie_id: str):
        with self._connection.cursor() as cursor:
            movie_cast = []
            cursor.execute(
                "SELECT memberID FROM movie_cast WHERE movieID = %s",
                (movie_id,)
            )
            cast_members_ids = [row[0] for row in cursor.fetchall()]
            for cast_member_id in cast_members_ids:
                movie_cast.append(self.get(cast_member_id))
            return movie_cast


    def get(self, member_id: str) -> CastMember:
        with self._connection.cursor() as cursor:
            return self.__get_single_entry(cursor, member_id)


    def create(self, entity: CastMember):
        self.execute_query(
            "INSERT INTO cast_member (memberID, dateOfBirth, countryCode) VALUES (%s, %s, %s)",
            (entity.get_member_id(), entity.date_of_birth, entity.get_country().get_country_code())
        )
        self.execute_query(
            "INSERT INTO cast_member_names (memberID, languageCode, memberName) VALUES (%s, %s, %s)",
            (entity.get_member_id(), lang, entity.member_name)
        )
        for position in entity.get_member_positions():
            self.execute_query(
                "INSERT INTO cast_members_positions (memberID, positionID) VALUES (%s, %s)",
                (entity.get_member_id(), position.get_position_id())
            )

    def update(self, entity: CastMember):
        self.execute_query(
            "UPDATE cast_member SET dateOfBirth = %s, countryCode = %s WHERE memberID = %s",
            (entity.date_of_birth, entity.get_country().get_country_code(), entity.get_member_id())
        )
        self.execute_query(
            "UPDATE cast_member_names SET memberName = %s WHERE memberID = %s AND languageCode = %s",
            (entity.member_name, entity.get_member_id(), lang)
        )

    def delete(self, entity: CastMember):
        self.execute_query(
            "DELETE FROM cast_member WHERE memberID = %s",
            (entity.get_member_id(),)
        )
        