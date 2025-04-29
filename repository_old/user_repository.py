from repository_old.base_repository import BaseRepository
from entity.user import User


class UserRepository(BaseRepository):
    def get_all(self) -> list[User]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cinema_user")
            rows = cursor.fetchall()
            return [User(*row) for row in rows]


    def get(self, user_id: str) -> User:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cinema_user WHERE userID ")
            row = cursor.fetchone()
            return User(*row)


    def find(self, name: str, surname: str) -> list[User]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM cinema_user WHERE userName = %s AND userSurname = %s",
                (name, surname)
            )
            rows = cursor.fetchall()
            return [User(*row) for row in rows]


    def create(self, entity: User):
        self.execute_query(
            "INSERT INTO cinema_user (userID, userLogin, userPassword, userName, userSurname, userRole) VALUES (%s, %s, %s, %s, %s, %s)",
            (entity.get_user_id(), entity.login, entity.password, entity.name, entity.surname, entity.get_role())
        )


    def update(self, entity: User):
        self.execute_query(
            "UPDATE cinema_user SET userLogin = %s, userPassword = %s, userName = %s, userSurname = %s, userRole = %s WHERE userID = %s",
            (entity.login, entity.password, entity.name, entity.surname, entity.get_role(), entity.get_user_id())
        )


    def delete(self, entity: User):
        self.execute_query(
            "DELETE FROM cinema_user WHERE userID = %s",
            (entity.get_user_id(),)
        )