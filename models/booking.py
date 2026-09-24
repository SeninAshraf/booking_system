from models.booking_status import BookingStatus
class booking:

    def __init__(self, bookingId,totalAmount,status,ticketQuantity):
        self.bookingId = bookingId
        self.totalAmount = totalAmount
        self.status = status
        self.ticketQuantity = ticketQuantity
    def display(self):
            print("booking id:",self.bookingId)
            print("total amount:",self.totalAmount)
            print("status:",self.status)
            print("ticket Quantity:",self.ticketQuantity)



    
    