class BookingController:
     def __init__(self, showservice,seatservice,bookingservice):
                    self.showservice = showservice
                    self.seatservice = seatservice
                    self.bookingservice = bookingservice

     def display_movie_details(self,choice,your_show,selected_seats):
             return self.bookingservice.display_movie_details(choice,your_show,selected_seats)

     def add_booking_details(self,customer_id,your_show,total_amount,num_tickets):
             return self.bookingservice.add_booking_details(customer_id,your_show,total_amount,num_tickets)

     def add_booking_seat_details(self,booking_id,selected_seat_id):
             return self.bookingservice.add_booking_seat_details(booking_id,selected_seat_id)