from models.booking_status import BookingStatus
from dao.bookingdao import BookingDAO
class booking:

    def __init__(self, bookingId,customerId,showId,totalAmount,status,ticketQuantity):
        self.bookingId = bookingId
        self.customerId= customerId
        self.showId= showId
        self.totalAmount = totalAmount
        self.status = status
        self.ticketQuantity = ticketQuantity
    def display(self):
            print("booking id:",self.bookingId)
            print("customer id:",self.customerId)
            print("show id:",self.showId)
            print("total amount:",self.totalAmount)
            print("status:",self.status)
            print("ticket Quantity:",self.ticketQuantity)

booking1 = booking(
    1,
    1,
    1,
    230,
    BookingStatus.CONFIRMED,
    2
)

booking_dao = BookingDAO()
#booking_dao.save(booking1)

print(booking_dao.find_all())
    
    