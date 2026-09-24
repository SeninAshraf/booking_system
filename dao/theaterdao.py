from database.connection import get_connection

class TheaterDao:
    def add_theater(self,theater):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO theater (theater_id,theater_name) VALUES (?,?)""",(theater.theater_id,theater.theaterName))
            connection.commit()
            connection.close()

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