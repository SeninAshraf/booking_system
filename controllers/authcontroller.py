class AuthenticationController:

    def __init__(self, authenticationservice,bookingservice):
        self.authenticationservice = authenticationservice
        self.bookingservice = bookingservice

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
    def customer_login(self,customer_mobile_num):
          return self.bookingservice.login_customer(
                customer_mobile_num
          )