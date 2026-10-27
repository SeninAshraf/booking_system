
import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch

from dao.bookingdao import BookingDAO


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

    def connect_test_db(self):
        connection = sqlite3.connect(self.db_path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def tearDown(self):
        self.patcher.stop()
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



