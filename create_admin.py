import bcrypt

from database.connection import get_connection

password = "123"

password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
).decode("utf-8")

connection = get_connection()
cursor = connection.cursor()
cursor.execute("""INSERT INTO admin (admin_username, password_hash) VALUES (?, ?)""", ("senin", password_hash))
connection.commit()
connection.close()
