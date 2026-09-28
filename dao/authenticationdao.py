from database.connection import get_connection
from models.admin import Admin
from models.theaterofficial import TheaterOfficial
from services.authenticationservice import AuthenticationService

class AuthDao:
    print("senin")
    def find_admin(self, username):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM admin WHERE admin_username = ?""", (username,))
        result = cursor.fetchone()
        connection.close()
        if result is None:
            return None
        else:
            return Admin(result[0], result[1])

    def find_theater_user(self,theater_name):
                    connection = get_connection()
                    cursor = connection.cursor()
                    cursor.execute("""select theater_user.theater_id,theater_user.username,theater_user.password_hash,theater_user.require_password_reset from theater_user join theater on theater_user.theater_id=theater.theater_id where theater_name=?""",(theater_name,))
                    result = cursor.fetchone()
                    connection.close()
                    
                    return TheaterOfficial(result[0], result[1],result[2],result[3])

    def changing_password(self,new_password_hash,theater_username, theater_name):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""UPDATE theater_user SET password_hash = ?,require_password_reset = 0 WHERE username = ? AND theater_id = (SELECT theater_id FROM theater WHERE theater_name = ?)""",(theater_name,theater_username,new_password_hash))
            connection.commit()
            connection.close()