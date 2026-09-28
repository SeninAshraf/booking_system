from database.connection import get_connection
from models.theaterofficial import TheaterOfficial
class TheaterOfficialDao:
    #def add_theateruser(self,theaterofficial):
            #connection = get_connection()
            #cursor = connection.cursor()
            #cursor.execute("""INSERT INTO theater_user (theater_id, username, password_hash, require_password_reset) VALUES (?, ?, ?, ?)""", (theaterofficial.theater_id,theaterofficial.theaterUserName,theaterofficial.passwordHash,theaterofficial.firstLogin))            
            #connection.commit()
            #connection.close()
            
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
                
                return TheaterOfficial(result[0], result[1],result[2],result[3])
            
   