from repository.base_repository import BaseRepository
from entity.genre import Genre

lang = 'RU'

class GenreRepository(BaseRepository):
    def get_all(self) -> list[Genre]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT gn.genreID, languageCode, genreName
                FROM genre as gn
                JOIN genre_names as gn_ns
                ON gn.genreID = gn_ns.genreID
                """
            )
            rows = cursor.fetchall()
            return [Genre(*row) for row in rows]

    def get(self, genre_id: str, language_code: str) -> Genre:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT gn.genreID, languageCode, genreName
                FROM genre as gn
                JOIN genre_names as gn_ns
                ON gn.genreID = gn_ns.genreID
                WHERE gn.genreID = %s
                AND languageCode = %s
                """,
                (genre_id, language_code)
            )
            row = cursor.fetchone()
            if row:
                return Genre(*row)
            return None


    def get_by_movie(self, movie_id: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT genreID FROM movie_genres WHERE movieID = %s",
                (movie_id,)
            )
            genre_ids = [row[0] for row in cursor.fetchall()]
            movie_genres = []
            for gen_id in genre_ids:
                movie_genres.append(self.get(gen_id, lang))
            return movie_genres


    def create(self, entity: Genre):
        self.execute_query(
            "INSERT INTO genre (genreID) VALUES (%s)",
            (entity.get_genre_id(),)
        )
        self.execute_query(
            "INSERT INTO genre_names (genre_id, languageCode, genreName) VALUES (%s, %s, %s)",
            (entity.get_genre_id(), entity.get_language_code(), entity.genre_name)
        )


    def update(self, entity: Genre):
        self.execute_query(
            "UPDATE genre_names SET genreName = %s WHERE genreID = %s AND languageCode = %s",
            (entity.genre_name, entity.get_genre_id(), entity.get_language_code())
        )


    def delete(self, entity: Genre):
        self.execute_query(
            "DELETE FROM genre WHERE genreID = %s",
            (entity.get_genre_id(), entity.get_language_code())
        )