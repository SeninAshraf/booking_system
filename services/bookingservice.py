class BookingService:
     def __init__(self, booking_dao):
            self.booking_dao = booking_dao

     def login_customer(self,customer_mobile_num):
           result = self.booking_dao.find_customer(customer_mobile_num)
           if result:
                 print("Existing user Found!!")
           else:
                 print("New User Detected!!!")
           return result

     def new_customer_login(self,customer_mobile_num):
           return self.booking_dao.save(customer_mobile_num)
           