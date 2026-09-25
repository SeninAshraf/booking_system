from models.seat_status import SeatStatus
from models.seat_category import SeatCategory
from dao.seatdao import SeatDAO
class seat:
    def __init__(self,seat_id,show_id,seat_no,category,seat_status,seat_price,seat_row):
        self.seat_id=seat_id
        self.show_id=show_id
        self.seat_no=seat_no
        self.category=category
        self.seat_status=seat_status
        self.seat_price=seat_price
        self.seat_row=seat_row
    def display(self):
        print("seat id:",self.seat_id)
        print("show id:",self.show_id)
        print("seat no:",self.seat_no)
        print("category:",self.category)
        print("seat status:",self.seat_status)
        print("seat price:",self.seat_price)
        print("seat row:",self.seat_row)

seat1=seat(1,1,"A10",SeatCategory.Economy,SeatStatus.available,250,"A")
seat_dao=SeatDAO()
seat_dao.update_status(seat1,SeatStatus.available)