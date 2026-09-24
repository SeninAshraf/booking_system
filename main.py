from models.seat_status import SeatStatus
from models.seat_category import SeatCategory
from models.seat import seat
from models.booking_status import BookingStatus
from models.booking import booking


booking1 = booking(
    1,
    230,
    BookingStatus.CONFIRMED,
    2
)

booking1.display()

seat1=seat(1,1,"A10",SeatCategory.ECONOMY,SeatStatus.available,250,"A")
seat1.display()


