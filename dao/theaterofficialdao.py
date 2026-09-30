from database.connection import get_connection
from models.theaterofficial import TheaterOfficial
class TheaterOfficialDao:

    def add_theateruser(self,theater_name,theater_username,password_hash):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO theater_user (theater_id, username, password_hash, require_password_reset) VALUES (?, ?, ?, 0)""", (theater_name,theater_username,password_hash))            
            connection.commit()
            connection.close()
            
    #def get_theater_user(self,theaterUserName):
            #connection = get_connection()
            #cursor = connection.cursor()
            #cursor.execute("""select * from theaterofficial where username=?""",(theaterUserName))
            #result= cursor.fetchone()
            #return result
    def find_theater_user(self,theater_name):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""select theater_user.theater_id,theater_user.username,theater_user.password_hash,theater_user.require_password_reset from theater_user join theater on theater_user.theater_id=theater.theater_id where theater_name=?""",(theater_name,))
        result = cursor.fetchone()
        connection.commit()
        connection.close()
                
        return True
    def get_theater_id(self, theater_name):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT theater_id FROM theater WHERE theater_name COLLATE NOCASE = ?""", (theater_name,))
        result = cursor.fetchone()
        connection.close()
        return result
            
   