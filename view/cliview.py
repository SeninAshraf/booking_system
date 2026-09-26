from dao.authenticationdao import AuthDao
from services.authenticationservice import AuthenticationService

auth_dao = AuthDao()
auth_service = AuthenticationService(auth_dao)

while True:

    username = input("Enter Username: ")

    password = input("Enter password: ")

    if auth_service.login_admin(username, password):
        print("Login successful")
        break

    print("Invalid username or password. Please try again.")