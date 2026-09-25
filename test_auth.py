from dao.authenticationdao import AuthDao

auth_dao = AuthDao()

admin = auth_dao.find_admin("senin")

if admin is None:
    print("Admin not found")
else:
    print("Admin found")
    print("Username:", admin.username)
    print("Password hash:", admin.passwordHash)