class TheaterController:

    def __init__(self, theater_service):
        self.theater_service = theater_service

    def theater_login(self, theater_name,theater_username,theater_password):
    
            return self.authenticationservice.login_admin(
                theater_name,
                theater_username,
                theater_password
            )