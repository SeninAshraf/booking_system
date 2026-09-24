from database.connection import get_connection

class MovieDao:
    def add_movie(self,movie):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO movie (movie_id,movie_title,movie_genre,movie_language,movie_duration,release_date,end_date) VALUES (?,?,?,?,?,?,?)""",(movie.movieId,movie.movieTitle,movie.movieGenre,movie.movieLanguage,movie.movieDuration,movie.releaseDate,movie.endDate))
        connection.commit()
        connection.close()

