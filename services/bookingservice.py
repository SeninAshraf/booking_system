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
#most confusing and struggled part
     def view_your_tickets(self,customer_mobile_num):
           result = self.booking_dao.view_your_tickets(customer_mobile_num)
            
    
           if not result:
                print("No tickets found.")
                return

           print("User found")
            #initialise variables
           previous_booking = None
           previous_total = None
          #(1, "Leo", "A5", 400) so row[0] = booking_id
           for row in result:
                booking_id = row[0]
                    #1!=None=tRUE
                if booking_id != previous_booking:
                        #FALSE SKIP
                    if previous_booking is not None:
                        print(f"\nTotal Amount : ₹{previous_total}")
                    #PRINT(MOVIE,SEAT: ONLY NO DATA,PRE=BOOK_ID,PREV_TOTAL=ROW[3])
                    print(f"\nMovie : {row[1]}")
                    print("Seats : ", end="")

                    previous_booking = booking_id
                    previous_total = row[3]
                #THEN IT CHANGE SEAT:A5
                print(row[2], end=" ")
                #THEN RETRUN TO FOR LOOP AGAIN BUT NO OTHER DATA SO 
            #TRUE THEN PRINT PREV BOOKING TOTAL AMOUNT,the final if prints the total for the last booking.
           if previous_booking is not None:
            print(f"\nTotal Amount : ₹{previous_total}")
        #FOR SPACE
           print()
           return True

     def view_all_transaction(self):
          result = self.booking_dao.view_all_transaction()
          if result:
               print(result)