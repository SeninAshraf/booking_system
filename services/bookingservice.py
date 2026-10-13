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

     def display_movie_details(self,choice,your_show,selected_seats):
           result = self.booking_dao.display_movie_details(choice,your_show,selected_seats)
           if result:
                 total_amount = 0
                 for row in result:
                       total_amount += row[3]
                 return result,total_amount
     def add_booking_details(self,customer_id,your_show,total_amount,num_tickets):
           return self.booking_dao.add_booking_details(customer_id,your_show,total_amount,num_tickets)

     def add_booking_seat_details(self,booking_id,selected_seat_id):
           return self.booking_dao.add_booking_seat_details(booking_id,selected_seat_id)

     def view_your_tickets(self,customer_mobile_num):
           result = self.booking_dao.view_your_tickets(customer_mobile_num)
           if result:
                print("User found")
                print(f"Movie : {result[0][0]}")

                print("Seats : ", end="")
                for row in result:
                    print(row[1], end=" ")

                print()
                print(f"Total Amount : ₹{result[0][2]:.0f}")
           else:
                print("User not found")