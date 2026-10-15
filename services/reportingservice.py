class ReportingService:
     def __init__(self, booking_dao):
                self.booking_dao = booking_dao
     def view_all_transaction(self):
               result = self.booking_dao.view_all_transaction()
               if not result:
                     print("No booking transactions found.")
                     return
               print("========== BOOKING TRANSACTIONS ==========")
               previous_booking = None
     
               for row in result:
                     booking_id = row[0]
     
                     if booking_id != previous_booking:
                         print(f"\nBooking ID: {row[0]}")
                         print(f"Customer Number: {row[1]}")
                         print(f"Movie Name: {row[2]}")
                         print(f"Show ID: {row[3]}")
                         print("Seats: ", end="")
                         previous_booking = booking_id
     
                     print(row[4], end=" ")#remove else because if we point else in this then it skip first seat name in first iteration
     
                     if row == result[-1] or result[result.index(row) + 1][0] != booking_id:#either it is in last row of tuple or next id of current row is new id any of these get true then pass total amount
                         print(f"\nTotal Amount: {row[5]}")
                         print(f"Booking Status: {row[6]}")
                         print()