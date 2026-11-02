from models.booking_status import BookingStatus
from dao.bookingdao import BookingDao
class Booking:

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


    