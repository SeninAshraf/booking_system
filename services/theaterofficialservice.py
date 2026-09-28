import bcrypt
class TheaterService:

    def __init__(self, theater_dao):
        self.theater_dao = theater_dao

    def login_user(self,theater_name,theater_username,theater_password):

        theater_user = self.theater_dao.find_theater_user(theater_name)

        if theater_user is None:
            return False

        return bcrypt.checkpw(
            theater_password.encode("utf-8"),
            theater_user.password_hash.encode("utf-8")
        )