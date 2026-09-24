import bcrypt
import sqlite3
connection = sqlite3.connect("movie_booking.db")

cursor = connection.cursor()
#cursor.execute("""create TABLE passw(name TEXT PRIMARY KEY,password_hash TEXT)""")
#connection.commit()
#connection.close()
#print("created  succesfully")

name= "senin123"
password = "senin"

password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print(password_hash)
password_hash = password_hash.decode("utf-8")

cursor.execute("""INSERT INTO passw (name, password_hash) VALUES (?, ?)""", (name, password_hash))
connection.commit()

print("User added successfully")

#connection.close()

name = input("Enter username: ")
password = input("Enter password: ")
cursor.execute("SELECT password_hash FROM passw WHERE name = ?",(name,))
result = cursor.fetchone()
if result is None:
    print("Username not found")
else:
    stored_hash = result[0]
    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode()
    ):
        print("Login successful")
    else:
        print("Wrong password")
connection.close()
