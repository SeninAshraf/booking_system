class AuthenticationController:

    def __init__(self, authenticationservice):
        self.authenticationservice = authenticationservice

    def login(self, username, password):

        return self.authenticationservice.login_admin(
            username,
            password
        )

    def theater_login(self, theater_name,theater_username,theater_password):
        
                return self.authenticationservice.login_user(
                    theater_name,
                    theater_username,
                    theater_password
                )