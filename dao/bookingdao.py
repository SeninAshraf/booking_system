from database.connection import get_connection
class BookingDAO:
    def save(self, booking):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO booking(booking_id,customer_id,show_id,total_amount,booking_status,ticket_quantity)VALUES (?, ?, ?, ?, ?, ?)""", (booking.bookingId,booking.customerId,booking.showId,booking.totalAmount,booking.status.value,booking.ticketQuantity))
        connection.commit()
        connection.close()

    def find_all(self):
        connection = get_connection()
        cursor= connection.cursor()
        cursor.execute("""select * from booking""")
        result = cursor.fetchall()
        return result
    
