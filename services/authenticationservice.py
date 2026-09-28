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

    def login_user(self,theater_name,theater_username,theater_password):
    
            theater_user = self.auth_dao.find_theater_user(theater_name)
    
            if theater_user is None:
                return False
    
            if not bcrypt.checkpw(
                theater_password.encode("utf-8"),
                theater_user.passwordHash.encode("utf-8")
            ):
                return False
            if theater_user.firstLogin:
                print("Password reset is required.")

                self.update_password(
                theater_name,
                theater_username
                )

            return True
    
    def update_password(self, theater_name, theater_username):
            new_password = input("Enter new password: ")

            new_password_hash = bcrypt.hashpw(
                    new_password.encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")

            self.auth_dao.changing_password(theater_name,theater_username,new_password_hash)
                            
            return True