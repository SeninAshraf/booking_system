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

     def view_your_tickets(self,customer_mobile_num):
             return self.bookingservice.view_your_tickets(customer_mobile_num)

     #def view_all_transaction(self):
             #return self.bookingservice.view_all_transaction()

     def view_show_based_theater(self, your_theater, choice):
        return self.showservice.view_show_based_theater(your_theater, choice)

     def view_seat_based_shows(self, your_show):
        return self.seatservice.view_seat_based_shows(your_show)

     def check_number_of_seats(self, your_show, num_tickets):
        return self.seatservice.check_number_of_seats(your_show, num_tickets)

     def update_booked_seats(self, your_show, selected_seats):
        return self.seatservice.update_booked_seats(your_show, selected_seats)