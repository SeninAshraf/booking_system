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
        cursor.execute("""SELECT * FROM seat WHERE show_id = ? ORDER BY seat_row,CAST(SUBSTR(seat_no, 2) AS INTEGER);""", (your_show,))
        result = cursor.fetchall()
        connection.close()
        return result


    def update_booked_seats(self, your_show, selected_seats):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            for seat_name in selected_seats:
                cursor.execute("""update seat set seat_status = 'Booked' where show_id = ? and seat_no = ? and seat_status = 'Available' """, (your_show, seat_name))
                if cursor.rowcount == 0:
                    connection.rollback()
                    return False
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            print("Error booking seats:", e)
            return False
        finally:
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