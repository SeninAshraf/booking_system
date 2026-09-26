import bcrypt

class AuthenticationService:

    def __init__(self, auth_dao):
        self.auth_dao = auth_dao

    def login_admin(self, username, password):

        admin = self.auth_dao.find_admin(username)

        if admin is None:
            return False

        return bcrypt.checkpw(
            password.encode("utf-8"),
            admin.passwordHash.encode("utf-8")
        )
