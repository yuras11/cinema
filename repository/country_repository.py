from repository.base_repository import BaseRepository
from entity.country import Country

lang = 'RU'


class CountryRepository(BaseRepository):
    def get_all(self) -> list[Country]:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ct.countryCode, languageCode, countryName
                FROM country as ct
                JOIN country_names as cn
                ON ct.countryCode = cn.countryCode 
                """
            )
            rows = cursor.fetchall()
            return [Country(*row) for row in rows]


    def get(self, country_code: str, language_code: str) -> Country:
        with self._connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT ct.countryCode, languageCode, countryName
                FROM country as ct
                JOIN country_names as cn
                ON ct.countryCode = cn.countryCode
                WHERE ct.countryCode = %s
                AND languageCode = %s
                """,
                (country_code, language_code)
            )
            row = cursor.fetchone()
            if row:
                return Country(*row)
            return None


    def get_by_movie(self, movie_id: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT countryCode FROM movie_countries WHERE movieID = %s",
                (movie_id,)
            )
            country_codes = [row[0] for row in cursor.fetchall()]
            movie_countries = []
            for country_code in country_codes:
                movie_countries.append(self.get(country_code, lang))
            return movie_countries


    def get_by_name(self, name: str):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM country_names WHERE countryName = %s",
                (name,)
            )
            row = cursor.fetchone()
            return Country(*row)


    def create(self, entity: Country):
        self.execute_query(
            "INSERT INTO country (countryCode) VALUES (%s)",
            (entity.get_country_code(),)
        )
        self.execute_query(
            "INSERT INTO country_names (countryCode, languageCode, countryName) VALUES (%s, %s, %s)",
            (entity.get_country_code(), entity.get_language_code(), entity.country_name)
        )


    def update(self, entity: Country):
        self.execute_query(
            "UPDATE country_names SET countryName = %s WHERE countryCode = %s AND languageCode = %s",
            (entity.country_name, entity.get_country_code(), entity.get_language_code())
        )


    def delete(self, entity: Country):
        self.execute_query(
            "DELETE FROM country WHERE countryCode = %s",
            (entity.get_country_code(), entity.get_language_code())
        )