import bcrypt
class TheaterService:

    def __init__(self, theater_dao):
        self.theater_dao = theater_dao

    def login_user(self,theater_name,theater_username,theater_password):

        theater_user = self.theater_dao.find_theater_user(theater_name)

        if theater_user is None:
            return False

        if not bcrypt.checkpw(
            theater_password.encode("utf-8"),
            theater_user.passwordHash.encode("utf-8")
        ):
            return False
        if theater_user.firstLogin:
            print("Password reset is required.")

        return True