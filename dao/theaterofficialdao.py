from database.connection import get_connection

class TheaterOfficialDao:
    def add_theateruser(self,theaterofficial):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO theater_user (theater_id, username, password_hash, require_password_reset) VALUES (?, ?, ?, ?)""", (theaterofficial.theater_id,theaterofficial.theaterUserName,theaterofficial.passwordHash,theaterofficial.firstLogin))            
            connection.commit()
            connection.close()
            
    def get_theater_user(self,theaterUserName):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""select * from theaterofficial where username=?""",(theaterUserName))
            result= cursor.fetchone()
            return result
          

   