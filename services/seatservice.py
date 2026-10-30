class SeatService:
    def __init__(self, seat_dao):
        self.seat_dao = seat_dao

    def add_seats(self,show_id,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
        for row in range(vip_rows):
            row_letter = chr(65 + row)

            for seat_number in range(1, vip_number_of_seats_per_row + 1):
                seat_no=f"{row_letter}{seat_number}"
                self.seat_dao.add_seat(
                    show_id,
                    seat_no,
                    "VIP",
                    "Available",
                    ticket_price_vip,
                    row_letter
                )

        for row in range(economy_rows):
                    row_letter = chr(65 + vip_rows + row)
        
                    for seat_number in range(1, economy_number_of_seat_per_row + 1):
                        seat_no=f"{row_letter}{seat_number}"
                        self.seat_dao.add_seat(
                            show_id,
                            seat_no,
                            "Economy",
                            "Available",
                            ticket_price_economy,
                            row_letter
                        )

        return True

    def update_seats(
                    self,
                    show_id,
                    vip_rows,
                    vip_seats,
                    vip_price,
                    economy_rows,
                    economy_seats,
                    economy_price
                ):

                self.seat_dao.delete_seats(show_id)

                for row in range(vip_rows):
                    row_letter = chr(65 + row)

                    for seat_number in range(1, vip_seats + 1):
                        seat_no = f"{row_letter}{seat_number}"

                        self.seat_dao.add_seat(
                            show_id,
                            seat_no,
                            "VIP",
                            "Available",
                            vip_price,
                            row_letter
                        )

                for row in range(economy_rows):
                    row_letter = chr(65 + vip_rows + row)

                    for seat_number in range(1, economy_seats + 1):
                        seat_no = f"{row_letter}{seat_number}"

                        self.seat_dao.add_seat(
                            show_id,
                            seat_no,
                            "Economy",
                            "Available",
                            economy_price,
                            row_letter
                        )

                return True

    def delete_seat(self,show_id):
         return self.seat_dao.delete_seats(show_id)

    def view_seat_based_shows(self,your_show):
          # Call the DAO method to retrieve all seats belonging to the selected show
         result= self.seat_dao.view_seat_based_shows(your_show)
         # Example: result contains all seats for show ID 10
         if result:
              # Display the heading for available seats
              print("====AVAILABLE SEATS====")
              # Create an empty list to store unique row letters
              rows = []
               # Example: []
                # Loop through every seat record returned from the database
              for seat in result:
                 # Check whether this seat's row letter is already in the rows list
                if seat[6] not in rows:
                     # Add the row letter if it is not already present
                    rows.append(seat[6])
                     # Example: ["A", "B", "C"]
             # Sort the row letters alphabetically
              rows.sort()
              # Example: ["C", "A", "B"] becomes ["A", "B", "C"]
               # Loop through each unique row letter
              for row in rows:
                 # Loop through all seat records again
                for seat in result:
                     # Check whether the seat belongs to the current row
                # AND whether its status is Available
                    if seat[6] == row and seat[4] == "Available":
                        # Print the seat number on the same line , end="" is for printing same line
                        print(seat[2], end=" ")
                         # Example: A1 A2 A3
 # Move to the next line after displaying the current row
                print()
                # Return all seat records to the method that called this method
              return result

    def check_number_of_seats(self,your_show,num_tickets):
         result = self.seat_dao.check_number_of_seats(your_show)
         if result >= num_tickets:#if there only 6 tickets and user enter 67 then it fail
              return True
         else:
              print("Ticket Availabilty Exceeds....!")
              return False

    def update_booked_seats(self,your_show,selected_seats):
         result = self.seat_dao.update_booked_seats(your_show,selected_seats)
         if result:
              return True