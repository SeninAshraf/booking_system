from database.connection import get_connection
class AuthDao:
    def find_admin(self, username):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM admin
            WHERE admin_username = ?
        """, (username,))

        result = cursor.fetchone()

        connection.close()

        return result