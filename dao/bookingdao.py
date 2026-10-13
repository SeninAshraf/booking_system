from database.connection import get_connection
class BookingDAO:
    def save(self, customer_mobile_number):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO customer(mobile_number)VALUES (?)""", (customer_mobile_number,))
        connection.commit()
        connection.close()
        return True

    def find_all(self):
        connection = get_connection()
        cursor= connection.cursor()
        cursor.execute("""select * from booking""")
        result = cursor.fetchall()
        return result

    def find_customer(self,customer_mobile_num):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""select customer_id from customer where mobile_number = ?""",(customer_mobile_num,))
        result =cursor.fetchone()
        return result

    def display_movie_details(self,choice,your_show,selected_seats):
        connection = get_connection()
        cursor = connection.cursor()
        result = []
        for seat_name in selected_seats:
            cursor.execute("""SELECT m.movie_title, s.show_id,seat.seat_no, seat.seat_price FROM movie m JOIN show s ON m.movie_id = s.movie_id JOIN seat ON s.show_id = seat.show_id WHERE m.movie_id = ? AND s.show_id = ? AND seat.seat_no = ?""", (choice,your_show, seat_name))
            result.extend(cursor.fetchall())
        return result

    def add_booking_details(self,customer_id,your_show,total_amount,num_tickets):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO booking(customer_id,show_id,total_amount,ticket_quantity,booking_status) VALUES (?,?,?,?,"Confirmed")""",(customer_id,your_show,total_amount,num_tickets,))
        connection.commit()
        connection.close()
        return True
