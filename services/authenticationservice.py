import bcrypt
class AuthenticationService:

    def __init__(self, auth_dao):
        self.auth_dao = auth_dao

    def login_admin(self, username, password):

        admin = self.auth_dao.find_admin(username)#CHECK ADMIN USERNAME

        if admin is None:
            return False#IF ADMIN NT PRESENT THEN RETURN FALSE

        return bcrypt.checkpw(#ELSE COMPARE NEW PASS AND STORED PASS AND RETURN
            password.encode("utf-8"),
            admin.passwordHash.encode("utf-8")
        )

    def login_user(self,theater_name,theater_username,theater_password):
    
            theater_user = self.auth_dao.find_theater_user(theater_name,theater_username)#check is any theater is existed
    
            if theater_user is None:#if theater didnt exist then nothing false only
                return False
    
            if not bcrypt.checkpw(#compared user enetered pass and stored pass
                theater_password.encode("utf-8"),
                theater_user.passwordHash.encode("utf-8")
            ):
                return False#if didnt match return false
            if theater_user.firstLogin:#if theater user only logged one time
                print("Password reset is required.")

                self.update_password(
                theater_name,
                theater_username#update pass function call with 2 inpu
                )

            return theater_user
    
    def update_password(self, theater_name, theater_username):
            new_password = input("Enter new password: ")

            new_password_hash = bcrypt.hashpw(#genrate random key or hash key
                    new_password.encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")

            self.auth_dao.changing_password(new_password_hash,theater_username,theater_name)#pass to dao to update pass
                            
            return True