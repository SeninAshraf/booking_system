class BookingController:
     def __init__(self, showservice,seatservice,bookingservice):
                    self.showservice = showservice
                    self.seatservice = seatservice
                    self.bookingservice = bookingservice

     def display_movie_details(self,choice,your_show,selected_seats):
             return self.bookingservice.display_movie_details(choice,your_show,selected_seats)