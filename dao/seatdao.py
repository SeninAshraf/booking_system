from database.connection import get_connection


class SeatDAO:

    def add_seat(self, show_id,seat_no,category,status,ticket_price,row_letter):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO seat(show_id, seat_no, category, seat_status, seat_price, seat_row) VALUES (?, ?, ?, ?, ?, ?)""", (show_id,seat_no,category,status,ticket_price,row_letter))
        connection.commit()
        connection.close()


    def find_by_show(self, show):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM seat WHERE show_id = ?""", (show.show_id,))
        result = cursor.fetchall()
        connection.close()
        return result


    def update_status(self, seat, status):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""UPDATE seat SET seat_status = ? WHERE seat_id = ?""", (status.value,seat.seat_id))
        connection.commit()
        connection.close()