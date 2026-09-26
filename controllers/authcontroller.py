class AuthenticationController:

    def __init__(self, authenticationservice):
        self.authenticationservice = authenticationservice

    def login(self, username, password):

        return self.authenticationservice.login_admin(
            username,
            password
        )