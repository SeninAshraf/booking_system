from database.connection import get_connection
from models.admin import Admin
from models.theaterofficial import TheaterOfficial

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
                    connection.commit()
                    connection.close()
                    
                    return TheaterOfficial(result[0], result[1],result[2],result[3])