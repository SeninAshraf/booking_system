from database.connection import get_connection

class MovieDao:
    def add_movie(self,movie):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO movie (movie_id,movie_title,movie_genre,movie_language,movie_duration,release_date,end_date) VALUES (?,?,?,?,?,?,?)""",(movie.movieId,movie.movieTitle,movie.movieGenre,movie.movieLanguage,movie.movieDuration,movie.releaseDate,movie.endDate))
        connection.commit()
        connection.close()

    def update_movie(self,movie):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""UPDATE movie SET movie_title = ?,movie_genre = ?,movie_language = ?,movie_duration = ?,release_date = ?,end_date = ? WHERE movie_id = ?""",(movie.movieTitle,movie.movieGenre,movie.movieLanguage,movie.movieDuration,movie.releaseDate,movie.endDate,movie.movieId))
            connection.commit()
            connection.close()

    def get_movie(self,movie_id):
        connection = get_connection()
        cursor=connection.cursor()
        cursor.execute("""SELECT * FROM movie where movie_id=?""",(movie_id,))
        result= cursor.fetchone()
        return result
        

