
import unittest
import sqlite3
import tempfile
import os
from datetime import date, timedelta
from unittest.mock import patch

from dao.moviedao import MovieDao
from dao.showdao import ShowDao
from dao.seatdao import SeatDAO
from services.movieservice import MovieService
from services.showservice import ShowService
from services.seatservice import SeatService
from controllers.moviecontroller import MovieController
from controllers.showcontroller import ShowController
from view.cliview import MovieView


class TestShowIntegration(unittest.TestCase):

    def setUp(self):
        fd, self.db_path = tempfile.mkstemp()#set up the db path temp
        os.close(fd)#close fd 

        connection = sqlite3.connect(self.db_path)#make connection to temp db path
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

            CREATE TABLE show (
                show_id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                theater_id INTEGER,
                screen_no INTEGER,
                start_time TEXT,
                end_time TEXT,
                show_date DATE
            );

            CREATE TABLE seat (
                seat_id INTEGER PRIMARY KEY,
                show_id INTEGER,
                seat_no TEXT,
                category TEXT,
                seat_status TEXT,
                seat_price REAL,
                seat_row TEXT,
                UNIQUE (show_id, seat_no)
            );
        """)#create 3 temp sql like movie,theater,seat,show

        today = date.today()#initailise todays date as today
        connection.execute(
            "INSERT INTO movie VALUES (1, ?, ?, ?, ?, ?, ?)",
            (
                "Inception", "Sci-Fi", "English", "148",
                (today + timedelta(days=1)).isoformat(),#add movies start date =today end date= 30+today
                (today + timedelta(days=30)).isoformat()
            )
        )
        connection.execute(
            "INSERT INTO theater VALUES (1, 'Grand Cinema')"#add values to theater
        )
        connection.commit()
        connection.close()

        def connect():
            return sqlite3.connect(self.db_path)
        self.patcher1 = patch(
                    "dao.moviedao.get_connection",
                    side_effect=connect
                )
        
        self.patcher2 = patch(
                            "dao.showdao.get_connection",
                            side_effect=connect
                        )
        self.patcher3 = patch(
                                    "dao.seatdao.get_connection",
                                    side_effect=connect
                                )
        self.patcher1.start()
        self.patcher2.start()
        self.patcher3.start()

        self.movie_dao = MovieDao()
        self.show_dao = ShowDao()
        self.seat_dao = SeatDAO()

        self.movie_controller = MovieController(
            MovieService(self.movie_dao)
        )
        self.show_controller = ShowController(
            ShowService(self.show_dao, self.movie_dao),
            SeatService(self.seat_dao)
        )
        self.view = MovieView()

    def test_create_show(self):#show creation
        show_date = (date.today() + timedelta(days=2)).isoformat()

        inputs = [
            "1", show_date, "1", "10:00", "12:00",
            "1", "2", "200",
            "2", "3", "100"
        ]
        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.view.configure_show(
                    self.movie_controller,
                    self.show_controller,
                    1#theater id
                )
        mock_print.assert_any_call(
            "Show and seats created successfully"
        )

        connection = sqlite3.connect(self.db_path)
        show_count = connection.execute(
            "SELECT COUNT(*) FROM show"
        ).fetchone()[0]
        seat_count = connection.execute(
            "SELECT COUNT(*) FROM seat"
        ).fetchone()[0]
        connection.close()

        self.assertEqual(show_count, 1)
        self.assertEqual(seat_count, 8)

    #test show before release date

    def test_show_before_release_date(self):
        # Choose a date before the movie's release date
        show_date = date.today().isoformat()

        inputs = [
            "1",          # Movie ID
            "1",          # Screen number
            show_date,    # Show date
            "10:00",      # Start time
            "12:00",      # End time
            "1", "2", "200",  # VIP configuration
            "2", "3", "100"   # Economy configuration
        ]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.view.configure_show(
                    self.movie_controller,
                    self.show_controller,
                    1
                )

        # The CLI should report that the show was not created
        mock_print.assert_any_call("Show was NOT created.")

        # Check that no show or seats were saved
        connection = sqlite3.connect(self.db_path)

        show_count = connection.execute(
            "SELECT COUNT(*) FROM show"
        ).fetchone()[0]

        seat_count = connection.execute(
            "SELECT COUNT(*) FROM seat"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(show_count, 0)
        self.assertEqual(seat_count, 0)
        
    def test_show_after_end_date(self):
        # Choose a date after the movie's end date
        show_date = "2026-12-16"

        inputs = [
            "1",          # Movie ID
            "1",          # Screen number
            show_date,    # Show date
            "10:00",      # Start time
            "12:00",      # End time
            "1", "2", "200",  # VIP configuration
            "2", "3", "100"   # Economy configuration
        ]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.view.configure_show(
                    self.movie_controller,
                    self.show_controller,
                    1
                )

        # Verify that the show was rejected
        mock_print.assert_any_call(
            "Show date must be on or before the movie end date"
        )

    def test_show_with_invalid_time(self):
        show_date = "2026-11-20"

        inputs = [
            "1",          # Movie ID
            "1",          # Screen number
            show_date,    # Show date
            "12:00",      # Start time
            "10:00",      # End time
            "1", "2", "200",  # VIP configuration
            "2", "3", "100"   # Economy configuration
        ]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.view.configure_show(
                    self.movie_controller,
                    self.show_controller,
                    1
                )

        # Verify that the invalid time range is rejected
        mock_print.assert_any_call(
            "End time must be after start time"
        )

    def tearDown(self):
        for p in self.patches:
            p.stop()
        os.remove(self.db_path)


if __name__ == "__main__":
    unittest.main()
