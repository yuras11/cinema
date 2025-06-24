from z_JUNK.repository_old.base_repository import BaseRepository
from z_JUNK.entity.position import Position


class PositionRepository(BaseRepository):
    def get_all(self) -> list[Position]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ps.positionID, languageCode, positionName 
                FROM positions as ps
                JOIN positions_names as p_ns
                ON ps.positionID = p_ns.positionID 
                """
            )
            rows = cursor.fetchall()
            return [Position(*row) for row in rows]


    def get(self, position_id: str, language_code: str) -> Position:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ps.positionID, languageCode, positionName 
                FROM positions as ps
                JOIN positions_names as p_ns
                ON ps.positionID = p_ns.positionID
                WHERE ps.positionID = %s
                AND languageCode = %s 
                """,
                (position_id, language_code)
            )
            row = cursor.fetchone()
            row[2] = row[2].strip()
            return Position(*row)


    def get_by_cast_member(self, member_id: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ps.positionID, languageCode, positionName 
                FROM positions as ps
                JOIN positions_names as p_ns
                ON ps.positionID = p_ns.positionID 
                JOIN cast_members_positions as c_m_p
                ON ps.positionID = c_m_p.positionID
                WHERE c_m_p.memberID = %s
                """,
                (member_id,)
            )
            rows = cursor.fetchall()
            return [Position(*row) for row in rows]


    def get_by_name(self, name: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ps.positionID, p_ns.languageCode, p_ns.positionName 
                FROM positions as ps
                JOIN positions_names as p_ns
                ON ps.positionID = p_ns.positionID
                WHERE p_ns.positionName = %s 
                """,
                (name,)
            )
            row = cursor.fetchone()
            return Position(*row)


    def create(self, entity: Position):
        self.execute_query(
            "INSERT INTO positions (position_id) VALUES (%s)",
            (entity.get_position_id(),)
        )
        self.execute_query(
            "INSERT INTO positions_names (position_id, languageCode, positionName) VALUES (%s, %s, %s)",
            (entity.get_position_id(), entity.get_language_code(), entity.position_name)
        )


    def update(self, entity: Position):
        self.execute_query(
            "UPDATE positions_names SET positionName = %s WHERE positionID = %s AND languageCode = %s",
            (entity.position_name, entity.get_position_id(), entity.get_language_code())
        )


    def delete(self, entity: Position):
        self.execute_query(
            "DELETE FROM positions WHERE positionID = %s",
            (entity.get_position_id(),)
        )