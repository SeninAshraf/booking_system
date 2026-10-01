from database.connection import get_connection
class TheaterOfficialDao:

    def add_theateruser(self,theater_id,theater_username,password_hash):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO theater_user (theater_id, username, password_hash, require_password_reset) VALUES (?, ?, ?, 0)""", (theater_id,theater_username,password_hash))            
            connection.commit()
            success = cursor.rowcount > 0
            connection.close()
            return success
    

    
    #def get_theater_user(self,theaterUserName):
            #connection = get_connection()
            #cursor = connection.cursor()
            #cursor.execute("""select * from theaterofficial where username=?""",(theaterUserName))
            #result= cursor.fetchone()
            #return result
    def find_theater_user(self,theater_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT theater_id,username,password_hash,require_password_reset FROM theater_user WHERE theater_id = ?""",(theater_id,))
        result = cursor.fetchone()
        connection.commit()
        connection.close()
        return result
                
        return True
    def get_theater_id(self, theater_name):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT theater_id FROM theater WHERE theater_name COLLATE NOCASE = ?""", (theater_name,))
        result = cursor.fetchone()
        connection.close()
        return result
            
   