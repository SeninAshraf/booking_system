import bcrypt
from dao.authenticationdao import AuthDao

auth_dao = AuthDao()

x=input('Enter Username:')
admin = auth_dao.find_admin(x)

if admin is None:
    print("Admin not found")
else:
   entered_password=input('Enter password:')
   if bcrypt.checkpw(entered_password.encode("utf-8"),
        admin.passwordHash.encode("utf-8")):
        print("Login successful")
   else:
        print("Wrong password")