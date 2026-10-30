from database.connection import get_connection
class BookingDAO:
    #def save(self, customer_mobile_number):
        #connection = get_connection()
        #cursor = connection.cursor()
        #cursor.execute("""INSERT INTO customer(mobile_number)VALUES (?)""", (customer_mobile_number,))
        #connection.commit()
        #connection.close()
        #return True

    def find_all(self):
        connection = get_connection()
        cursor= connection.cursor()
        cursor.execute("""select * from booking""")
        result = cursor.fetchall()
        return result

    #def find_customer(self,customer_mobile_num):
        #connection = get_connection()
        #cursor = connection.cursor()
        #cursor.execute("""select customer_id from customer where mobile_number = ?""",(customer_mobile_num,))
        #result =cursor.fetchone()
        #return result

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
        booking_id = cursor.lastrowid
        connection.close()
        return booking_id

    def add_booking_seat_details(self,booking_id,selected_seat_id):
        connection = get_connection()
        cursor = connection.cursor()
        for id in selected_seat_id:
            cursor.execute("""insert into booking_seat(booking_id,seat_id) values(?,?)""",(booking_id,id))
        connection.commit()
        connection.close()
        return True

    def view_your_tickets(self,customer_mobile_num):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""select b.booking_id,m.movie_title,seat.seat_no,b.total_amount FROM movie m JOIN show s ON m.movie_id=s.movie_id JOIN seat on s.show_id=seat.show_id JOIN booking_seat  on seat.seat_id =booking_seat.seat_id JOIN booking b on booking_seat.booking_id=b.booking_id JOIN customer on b.customer_id=customer.customer_id where mobile_number=? order by b.booking_id""",(customer_mobile_num,))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def view_all_transaction(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT b.booking_id,c.mobile_number,m.movie_title,s.show_id,seat.seat_no,b.total_amount,b.booking_status FROM customer c JOIN booking b ON c.customer_id = b.customer_id JOIN show s ON b.show_id = s.show_id JOIN movie m ON s.movie_id = m.movie_id JOIN booking_seat bs ON b.booking_id = bs.booking_id JOIN seat ON bs.seat_id = seat.seat_id""")
        result=cursor.fetchall()
        connection.commit()
        connection.close()
        return result