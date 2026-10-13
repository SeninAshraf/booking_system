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
            
    
           if not result:
                print("No tickets found.")
                return

           print("User found")

           previous_booking = None

           for row in result:
                booking_id = row[0]

                if booking_id != previous_booking:
                    print(f"\nMovie : {row[1]}")
                    print("Seats : ", end="")
                    print(row[2], end=" ")
                    print(f"\nTotal Amount : ₹{row[3]}")

                    previous_booking = booking_id
                else:
                    print(row[2], end=" ")#if booking_id= previous booking and want to append other seat also so this use

           print()