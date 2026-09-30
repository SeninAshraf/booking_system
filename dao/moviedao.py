from database.connection import get_connection

class MovieDao:
    def add_movie(self,title,genre,language,duration,release_date,end_date):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO movie (movie_title,movie_genre,movie_language,movie_duration,release_date,end_date) VALUES (?,?,?,?,?,?)""",(title,genre,language,duration,release_date,end_date))
        connection.commit()
        connection.close()
        return True

    def update_movie(self,title1,genre1,language1,duration1,release_date1,end_date1,movie_id):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""UPDATE movie SET movie_title = ?,movie_genre = ?,movie_language = ?,movie_duration = ?,release_date = ?,end_date = ? WHERE movie_id = ?""",(title1,genre1,language1,duration1,release_date1,end_date1,movie_id))
            connection.commit()
            connection.close()

    def get_movie(self,movie_id):
        connection = get_connection()
        cursor=connection.cursor()
        cursor.execute("""SELECT * FROM movie where movie_id=?""",(movie_id,))
        result= cursor.fetchone()
        return result

    def delete_movie(self,movie_id):
            connection = get_connection()
            cursor=connection.cursor()
            cursor.execute("""DELETE from movie where movie_id=?""",(movie_id,))
            connection.commit()
            connection.close()
            return True
   
    def view_movie(self):
            connection = get_connection()
            cursor=connection.cursor()
            cursor.execute("""SELECT movie_id,movie_title from movie""")
            result= cursor.fetchall()
            return result

