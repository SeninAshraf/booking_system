from database.connection import get_connection

class ShowDao:
    def add_show(self,screen_number,start_time,end_time,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
                connection = get_connection()
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO show (movie_id, theater_id, screen_no,start_time,end_time,show_date) VALUES (?, ?, ?, ?,?,?)""", (show.movieId,show.theater_id,show.screenNo,show.startTime,show.endTime,show.showDate))            
                connection.commit()
                connection.close()

    def update_show(self,show):
                connection = get_connection()
                cursor = connection.cursor()
                cursor.execute("""UPDATE show SET movie_id=?,theater_id=?,screen_no=?,start_time=?,end_time=?,show_date=? WHERE show_id=?""",(show.movieId,show.theater_id,show.screenNo,show.startTime,show.endTime,show.showDate,show.showId))
                connection.commit()
                connection.close()

    def delete_show(self,showId):
                connection = get_connection()
                cursor=connection.cursor()
                cursor.execute("""DELETE from show where show_id=?""",(showId,))
                connection.commit()
                connection.close()

    def get_all(self):
            connection = get_connection()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM show")
            result = cursor.fetchall()
            return result

    