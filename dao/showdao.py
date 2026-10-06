from database.connection import get_connection

class ShowDao:
    def add_show(self,choice,theater_id,screen_no,start_time,end_time,show_date):
                connection = get_connection()
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO show (movie_id, theater_id, screen_no,start_time,end_time,show_date) VALUES (?, ?, ?, ?,?,?)""", (choice,theater_id,screen_no,start_time,end_time,show_date))
                show_id = cursor.lastrowid
                connection.commit()
                connection.close()
                return show_id

    def check_show_collision(self,theater_id,screen_number,show_date,start_time,end_time):
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""select show_id from show where theater_id =? and screen_no=? and show_date=? and start_time<? and end_time>?""",(theater_id,screen_number,show_date,end_time,start_time))
            result = cursor.fetchone()
            connection.close()
            return result
    
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

    