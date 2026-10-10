from database.connection import get_connection

class TheaterDao:
    def add_theater(self,theater_name):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO theater (theater_name) VALUES (?)""",(theater_name,))
            connection.commit()
            theater_id = cursor.lastrowid
            connection.close()
            return theater_id

    def update_theater(self,theater):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""UPDATE theater SET theater_name=? WHERE theater_id=?""",(theater.theaterName,theater.theater_id))
            connection.commit()
            connection.close()

    def get_theater(self,theater_name):
            connection = get_connection()
            cursor=connection.cursor()
            cursor.execute("""SELECT * FROM theater where theater_name COLLATE NOCASE =?""",(theater_name,))
            result= cursor.fetchone()
            return result

    def view_theaters(self):
           connection = get_connection()
           cursor = connection.cursor()
           cursor.execute("""SELECT * FROM theater""")
           result = cursor.fetchall()
           return result

    def view_movie_based_theater(self,choice):
           connection = get_connection()
           cursor = connection.cursor()
           cursor.execute("""select t.theater_id,t.theater_name from theater t JOIN show s on t.theater_id = s.theater_id where s.movie_id=?""",(choice,))
           result = cursor.fetchall()
           return result