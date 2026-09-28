import bcrypt

from database.connection import get_connection

password = "12344"

password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
).decode("utf-8")

connection = get_connection()
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO theater (theater_name) VALUES (?)""",
    ("MARS",)
)

#returning of id generation of auto generated primary key in theater table
theater_id = cursor.lastrowid


cursor.execute(
    """INSERT INTO theater_user
       (theater_id, username, password_hash, require_password_reset)
       VALUES (?, ?, ?, ?)""",
    (theater_id, "mars_01", password_hash, True)
)

connection.commit()
connection.close()

print("Theater and theater user created successfully")