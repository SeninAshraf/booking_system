
import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch

from dao.bookingdao import BookingDAO
from dao.seatdao import SeatDAO


class TestBookingIntegration(unittest.TestCase):

    def setUp(self):
        fd, self.db_path = tempfile.mkstemp()
        os.close(fd)

        connection = sqlite3.connect(self.db_path)
        connection.execute("PRAGMA foreign_keys = ON")

        connection.executescript("""
            CREATE TABLE movie (
                movie_id INTEGER PRIMARY KEY,
                movie_title TEXT,
                movie_genre TEXT,
                movie_language TEXT,
                movie_duration TEXT,
                release_date DATE,
                end_date DATE
            );

            CREATE TABLE theater (
                theater_id INTEGER PRIMARY KEY,
                theater_name TEXT
            );

            CREATE TABLE customer (
                customer_id INTEGER PRIMARY KEY,
                mobile_number TEXT
            );

            CREATE TABLE show (
                show_id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                theater_id INTEGER,
                screen_no INTEGER,
                start_time TEXT,
                end_time TEXT,
                show_date DATE,
                FOREIGN KEY (movie_id) REFERENCES movie(movie_id),
                FOREIGN KEY (theater_id) REFERENCES theater(theater_id)
            );

            CREATE TABLE seat (
                seat_id INTEGER PRIMARY KEY,
                show_id INTEGER,
                seat_no TEXT,
                category TEXT CHECK (category IN ('Economy', 'VIP')),
                seat_status TEXT,
                seat_price REAL,
                seat_row TEXT,
                FOREIGN KEY (show_id) REFERENCES show(show_id),
                UNIQUE (show_id, seat_no)
            );

            CREATE TABLE booking (
                booking_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                show_id INTEGER,
                total_amount INTEGER,
                ticket_quantity INTEGER,
                booking_status TEXT CHECK (
                    booking_status IN ('Confirmed')
                ),
                FOREIGN KEY (customer_id)
                    REFERENCES customer(customer_id),
                FOREIGN KEY (show_id)
                    REFERENCES show(show_id)
            );

            CREATE TABLE booking_seat (
                booking_seat_id INTEGER PRIMARY KEY,
                booking_id INTEGER,
                seat_id INTEGER,
                FOREIGN KEY (booking_id)
                    REFERENCES booking(booking_id),
                FOREIGN KEY (seat_id)
                    REFERENCES seat(seat_id),
                UNIQUE (seat_id)
            );
        """)

        connection.executescript("""
            INSERT INTO movie VALUES (
                1, 'Inception', 'Sci-Fi', 'English',
                '148', '2026-01-01', '2026-12-31'
            );

            INSERT INTO theater VALUES (1, 'Grand Cinema');

            INSERT INTO customer VALUES (1, '9876543210');

            INSERT INTO show VALUES (
                1, 1, 1, 1, '10:00', '12:00', '2026-11-20'
            );

            INSERT INTO seat VALUES
                (1, 1, 'A1', 'VIP', 'Available', 200, 'A'),
                (2, 1, 'A2', 'VIP', 'Available', 200, 'A');
        """)

        connection.commit()
        connection.close()

        self.patcher = patch(
            "dao.bookingdao.get_connection",
            side_effect=self.connect_test_db
        )
        self.patcher.start()

        self.dao = BookingDAO()
        self.seat_patcher = patch(
            "dao.seatdao.get_connection",
            side_effect=self.connect_test_db
        )
        self.seat_patcher.start()

        self.seat_dao = SeatDAO()

    def connect_test_db(self):
        connection = sqlite3.connect(self.db_path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def tearDown(self):
        self.patcher.stop()
        self.seat_patcher.stop()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_add_booking_details(self):
        booking_id = self.dao.add_booking_details(
            customer_id=1,
            your_show=1,
            total_amount=400,
            num_tickets=2
        )

        self.assertIsNotNone(booking_id)#for getting booking_id

        connection = self.connect_test_db()
        result = connection.execute(
            "SELECT total_amount, ticket_quantity, booking_status "
            "FROM booking WHERE booking_id = ?",
            (booking_id,)
        ).fetchone()
        connection.close()

        self.assertEqual(result, (400, 2, "Confirmed"))#check is that added

    def test_add_booking_seat_details(self):
        booking_id = self.dao.add_booking_details(1, 1, 400, 2)

        result = self.dao.add_booking_seat_details(
            booking_id, [1, 2]#[1,2] is seat_id
        )

        self.assertTrue(result)

        connection = self.connect_test_db()
        rows = connection.execute(
            "SELECT seat_id FROM booking_seat "
            "WHERE booking_id = ? ORDER BY seat_id",
            (booking_id,)
        ).fetchall()
        connection.close()#check only 1,2 is avail

        self.assertEqual(rows, [(1,), (2,)])

    def test_display_movie_details(self):
        result = self.dao.display_movie_details(
            choice=1,
            your_show=1,
            selected_seats=["A1", "A2"]
        )

        expected = [
            ("Inception", 1, "A1", 200.0),
            ("Inception", 1, "A2", 200.0)
        ]

        self.assertEqual(result, expected)

    def test_find_customer(self):
        result = self.dao.find_customer("9876543210")

        self.assertEqual(result, (1,))

    def test_save_customer(self):
        result = self.dao.save("9123456780")

        self.assertTrue(result)

        connection = self.connect_test_db()
        customer = connection.execute(
            "SELECT mobile_number FROM customer WHERE mobile_number = ?",
            ("9123456780",)
        ).fetchone()
        connection.close()

        self.assertEqual(customer, ("9123456780",))

    
    def test_customer_book_tickets(self):
        # Step 1: Find the customer
        customer = self.dao.find_customer("9876543210")
        self.assertIsNotNone(customer)#find already added customer

        customer_id = customer[0]#retrieve customer id

        # Step 2: Retrieve details for the selected seats
        selected_seats = ["A1", "A2"]#select seats

        movie_details = self.dao.display_movie_details(
            choice=1,
            your_show=1,
            selected_seats=selected_seats
        )#display details of selected seats

        self.assertEqual(len(movie_details), 2)#check is that 2 seats were returned

        # Step 3: Calculate the total ticket price
        total_amount = sum(row[3] for row in movie_details)
        self.assertEqual(total_amount, 400)#calculate sum and check is that equal to 400

        # Step 4: Get the database IDs of the selected seats
        connection = self.connect_test_db()

        selected_seat_ids = [
            row[0] for row in connection.execute(
                """
                SELECT seat_id
                FROM seat
                WHERE show_id = ?
                AND seat_no IN (?, ?)
                ORDER BY seat_no
                """,
                (1, "A1", "A2")
            ).fetchall()
        ]#select seat_id

        connection.close()

        self.assertEqual(len(selected_seat_ids), 2)#heck no seats is 2

        # Step 5: Mark the selected seats as booked
        result = self.seat_dao.update_booked_seats(
            your_show=1,
            selected_seats=selected_seats
        )
#update selected seats status
        self.assertTrue(result)

        # Step 6: Save the booking
        booking_id = self.dao.add_booking_details(
            customer_id=customer_id,
            your_show=1,
            total_amount=total_amount,
            num_tickets=len(selected_seats)
        )#add booking details and retrive bookin_id

        self.assertIsNotNone(booking_id)#ensure booking_id is returned

        # Step 7: Link the seats to the booking
        result = self.dao.add_booking_seat_details(#add booking seat_details to get booking_seat_id
            booking_id,
            selected_seat_ids
        )

        self.assertTrue(result)

        # Step 8: Verify the saved booking
        connection = self.connect_test_db()

        booking = connection.execute(
            """
            SELECT customer_id, show_id, total_amount,
                ticket_quantity, booking_status
            FROM booking
            WHERE booking_id = ?
            """,
            (booking_id,)
        ).fetchone()

        booked_seats = connection.execute(
            """
            SELECT seat_id
            FROM booking_seat
            WHERE booking_id = ?
            ORDER BY seat_id
            """,
            (booking_id,)
        ).fetchall()

        seat_statuses = connection.execute(
            """
            SELECT seat_no, seat_status
            FROM seat
            WHERE show_id = 1
            ORDER BY seat_no
            """
        ).fetchall()

        connection.close()

        self.assertEqual(
            booking,
            (customer_id, 1, 400, 2, "Confirmed")
        )

        self.assertEqual(
            booked_seats,
            [(1,), (2,)]
        )

        self.assertEqual(
            seat_statuses,
            [("A1", "Booked"), ("A2", "Booked")]
        )

    def test_customer_login_existing_user(self):
        # Customer already exists in the temporary database
        result = self.dao.find_customer("9876543210")

        self.assertIsNotNone(result)
        self.assertEqual(result, (1,))


    def test_customer_login_new_user(self):
        result = self.dao.find_customer("0000000000")

        self.assertIsNone(result)
