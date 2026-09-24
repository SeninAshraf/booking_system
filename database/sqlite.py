import sqlite3
connection = sqlite3.connect("movie_booking.db")

#cursor = connection.cursor()
#cursor.execute("""create TABLE customer(customer_id INTEGER PRIMARY KEY,mobile_number CHAR, UNIQUE)""")
#connection.commit()
#connection.close()
#print("created  succesfully")


#cursor = connection.cursor()
#cursor.execute("""create TABLE movie(movie_id INTEGER PRIMARY KEY,movie_title TEXT,movie_genre TEXT,movie_language TEXT,movie_duration TEXT,release_date DATE,end_date DATE)""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""create TABLE theater_user(theater_user_id INTEGER PRIMARY KEY,theater_id INTEGER,username TEXT UNIQUE,password_hash TEXT,require_password_reset BOOLEAN,FOREIGN KEY (theater_id) REFERENCES theater(theater_id))""")
#connection.commit()

#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""create TABLE theater(theater_id INTEGER PRIMARY KEY,theater_user_id INTEGER,theater_name TEXT UNIQUE,FOREIGN KEY (theater_user_id) REFERENCES theater_user(theater_user_id))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""CREATE TABLE show (show_id INTEGER PRIMARY KEY,movie_id INTEGER,theater_id INTEGER,screen_no INTEGER,start_time TEXT,end_time TEXT,show_date DATE,FOREIGN KEY (movie_id) REFERENCES movie(movie_id),FOREIGN KEY (theater_id) REFERENCES theater(theater_id))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""CREATE TABLE seat (seat_id INTEGER PRIMARY KEY,show_id INTEGER,seat_no TEXT,category TEXT CHECK (category IN ('Economy', 'VIP')),seat_status TEXT,seat_price REAL,seat_row TEXT,FOREIGN KEY (show_id) REFERENCES show(show_id),UNIQUE (show_id, seat_no))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""CREATE TABLE booking (booking_id INTEGER PRIMARY KEY,customer_id INTEGER,show_id INTEGER,total_amount INTEGER,ticket_quantity INTEGER,FOREIGN KEY (customer_id) REFERENCES customer(customer_id),FOREIGN KEY (show_id) REFERENCES show(show_id))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""CREATE TABLE booking_seat (booking_seat_id INTEGER PRIMARY KEY,booking_id INTEGER,seat_id INTEGER,FOREIGN KEY (booking_id) REFERENCES booking(booking_id),FOREIGN KEY (seat_id) REFERENCES seat(seat_id),UNIQUE (seat_id))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""CREATE TABLE admin (admin_username TEXT ,password_hash TEXT,UNIQUE(admin_username))""")
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""
    #UPDATE movie
   # SET release_date = '2026-10-04',
    #    end_date = '2026-11-04'
    #WHERE movie_id = 1
#""")

#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""select movie_duration from movie where movie_id = 1""")
#row = cursor.fetchall()
#print(row)
#connection.commit()
#connection.close()
#print("created  succesfully")

#cursor = connection.cursor()
#cursor.execute("""insert into customer (customer_id,mobile_number) values (1,"9633740775")""")
#connection.commit()
#connection.close()
#print("created  succesfully")


