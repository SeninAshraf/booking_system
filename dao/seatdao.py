from database.connection import get_connection


class SeatDAO:

    def add_seat(self, show_id,seat_no,category,status,ticket_price,row_letter):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO seat(show_id, seat_no, category, seat_status, seat_price, seat_row) VALUES (?, ?, ?, ?, ?, ?)""", (show_id,seat_no,category,status,ticket_price,row_letter))
        connection.commit()
        connection.close()
        return True

    def view_seat_based_shows(self,your_show ):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM seat WHERE show_id = ?""", (your_show,))
        result = cursor.fetchall()
        connection.close()
        return result


    def update_status(self, seat, status):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""UPDATE seat SET seat_status = ? WHERE seat_id = ?""", (status.value,seat.seat_id))
        connection.commit()
        connection.close()

    def delete_seats(self, show_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM seat WHERE show_id = ?",
            (show_id,)
        )

        connection.commit()
        connection.close()

        return True

    def check_number_of_seats(self,your_show):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""select count(seat_id) from seat where seat_status = 'Available' and show_id =?""",(your_show,))
        result = cursor.fetchone()[0]
        connection.commit()
        return result