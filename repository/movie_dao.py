from repository.base_repository import BaseRepository
from repository.cast_member_dao import CastMemberRepository
from repository.country_dao import CountryRepository
from repository.genre_dao import GenreRepository
from entity.movie import Movie

lang = 'RU'

class MovieRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self.__country_dao = CountryRepository(connection)
        self.__cast_member_dao = CastMemberRepository(connection)
        self.__genre_dao = GenreRepository(connection)

    def __get_single_entry(self, cursor, movie_id):
        cursor.execute("SELECT * FROM movie WHERE movieID = %s", (movie_id,))
        movie_id, duration, release_date, age_rate = cursor.fetchone()
        # getting name
        cursor.execute(
            "SELECT movieName FROM movie_name WHERE movieID = %s AND languageCode = %s",
            (movie_id, lang)
        )
        movie_name = cursor.fetchone()[0].strip()

        # getting countries
        movie_countries = self.__country_dao.get_by_movie(movie_id)

        # getting genres
        movie_genres = self.__genre_dao.get_by_movie(movie_id)

        # getting cast
        movie_cast = self.__cast_member_dao.get_by_movie(movie_id)

        return Movie(movie_id, movie_name, movie_countries, movie_genres, movie_cast, duration, release_date, age_rate)


    def get_all(self) -> list[Movie]:
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT movieID FROM movie")
            movie_ids = [row[0] for row in cursor.fetchall()]
            movies = []
            for movie_id in movie_ids:
                movies.append(self.__get_single_entry(cursor, movie_id))
            return movies


    def get(self, movie_id: str) -> Movie:
        with self._connection.cursor() as cursor:
            return self.__get_single_entry(cursor, movie_id)


    def get_by_cast_member(self, member_id: str):
        with self._connection.cursor() as cursor:
            cursor.execute("SELECT movieID FROM movie_cast WHERE memberID = %s", (member_id,))
            movie_ids = [row[0] for row in cursor.fetchall()]
            movies = []
            for movie_id in movie_ids:
                movies.append(self.__get_single_entry(cursor, movie_id))
            return movies


    def get_by_country(self, country_code: str) -> list[Movie]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT movieID FROM movie_countries WHERE countryCode = %s",
                (country_code,)
            )
            movie_ids = [row[0] for row in cursor.fetchall()]
            movie_list = []
            for movie_id in movie_ids:
                movie_list.append(self.__get_single_entry(cursor, movie_id))

            return movie_list


    def create(self, entity: Movie):
        self.execute_query(
            "INSERT INTO movie (movieID, duration, releaseDate, ageRate) VALUES (%s, %s, %s, %s)",
            (entity.get_movie_id(), entity.duration, entity.get_release_date(), entity.get_age_rate())
        )
        self.execute_query(
            "INSERT INTO movie_names (movieID, languageCode, movieName) VALUES (%s, %s, %s)",
            (entity.get_movie_id(), lang, entity.get_movie_name())
        )
        for genre in entity.get_movie_genres():
            self.execute_query(
                "INSERT INTO movie_genres (movieID, genreID) VALUES (%s, %s)",
                (entity.get_movie_id(), genre.get_genre_id())
            )
        for country in entity.get_movie_countries():
            self.execute_query(
                "INSERT INTO movie_countries (movieID, countryCode) VALUES (%s, %s)",
                (entity.get_movie_id(), country.get_country_code())
            )
        for cast_member in entity.get_movie_cast():
            self.execute_query(
                "INSERT INTO movie_cast (movieID, memberID) VALUES (%s, %s)",
                (entity.get_movie_id(), cast_member.get_member_id())
            )


    def update(self, entity: Movie):
        self.execute_query(
            "UPDATE movie_name SET movieName = %s WHERE movieID = %s AND languageCode = %s",
            (entity.get_movie_name(), entity.get_movie_id(), lang)
        )


    def delete(self, entity: Movie):
        self.execute_query(
            "DELETE FROM movie WHERE movieID = %s",
            (entity.get_movie_id(),)
        )