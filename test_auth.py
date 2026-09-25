import bcrypt
from dao.authenticationdao import AuthDao

auth_dao = AuthDao()

while True:
    username = input("Enter Username: ")
    admin = auth_dao.find_admin(username)
    if admin is None:
        print("Admin not found. Please try again.")
        continue
    entered_password = input("Enter password: ")
    if bcrypt.checkpw(
        entered_password.encode("utf-8"),
        admin.passwordHash.encode("utf-8")
    ):
        print("Login successful")
        break
    else:
        print("Wrong password. Please try again.")