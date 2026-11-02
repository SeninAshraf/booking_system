class BookingController:
     def __init__(self, showservice,seatservice,bookingservice,theaterservice):
                    self.showservice = showservice
                    self.seatservice = seatservice
                    self.bookingservice = bookingservice
                    self.theaterservice = theaterservice   

     def display_movie_details(self,movie_id,show_id,selected_seats):
             return self.bookingservice.display_movie_details(movie_id,show_id,selected_seats)

     def add_booking_details(self,customer_id,show_id,total_amount,num_tickets):
             return self.bookingservice.add_booking_details(customer_id,show_id,total_amount,num_tickets)

     def add_booking_seat_details(self,booking_id,selected_seat_id):
             return self.bookingservice.add_booking_seat_details(booking_id,selected_seat_id)

     def view_your_tickets(self,customer_mobile_num):
             return self.bookingservice.view_your_tickets(customer_mobile_num)

     #def view_all_transaction(self):
             #return self.bookingservice.view_all_transaction()

     def view_show_based_theater(self, theater_id, movie_id):
        return self.showservice.view_show_based_theater(theater_id, movie_id)

     def view_seat_based_shows(self, show_id):
        return self.seatservice.view_seat_based_shows(show_id)

     def check_number_of_seats(self, show_id, num_tickets):
        return self.seatservice.check_number_of_seats(show_id, num_tickets)

     def update_booked_seats(self, show_id, selected_seats):
        return self.seatservice.update_booked_seats(show_id, selected_seats)

     def view_movie_based_theater(self, movie_id):
        return self.theaterservice.view_movie_based_theater(movie_id)