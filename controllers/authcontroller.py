class AuthenticationController:
#CONSTRUCTOR=method that initializes an object when you create it
    def __init__(self, authenticationservice,bookingservice):#runs automatically when you create an object of the class. It receives the two service objects you pass in.
        self.authenticationservice = authenticationservice#1. The controller now has a reference to that same service object, allowing it to call its methods.
        self.bookingservice = bookingservice

    def login(self, username, password):#MOVE TO SERVICE LOGIN METHOD

        return self.authenticationservice.login_admin(
            username,
            password
        )#RETRUN GIVEN RESULT

    def theater_login(self, theater_name,theater_username,theater_password):#pass to service with 3 service
        
                return self.authenticationservice.login_user(
                    theater_name,
                    theater_username,
                    theater_password
                )
    def customer_login(self,customer_mobile_num):#pas to booking_service login_customer with cust mobile num parameter
          return self.authenticationservice.login_customer(
                customer_mobile_num
          )

    def new_customer_login(self,customer_mobile_num):#pass to new_customer in booking service
          return self.authenticationservice.new_customer_login(customer_mobile_num)