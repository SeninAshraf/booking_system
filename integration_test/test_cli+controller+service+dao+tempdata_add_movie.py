
import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch

from dao.moviedao import MovieDao
from services.movieservice import MovieService
from controllers.moviecontroller import MovieController
from view.cliview import MovieView


class TestMovieFullIntegration(unittest.TestCase):

    def setUp(self):
        fd, self.db_path = tempfile.mkstemp()
        os.close(fd)

        connection = sqlite3.connect(self.db_path)
        connection.execute("""
            CREATE TABLE movie (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_title TEXT,
                movie_genre TEXT,
                movie_language TEXT,
                movie_duration INTEGER,
                release_date TEXT,
                end_date TEXT
            )
        """)
        connection.close()

        def create_connection():
            return sqlite3.connect(self.db_path)

        self.patcher = patch(
            "dao.moviedao.get_connection",
            side_effect=create_connection
        )
        self.patcher.start()

        self.dao = MovieDao()
        self.service = MovieService(self.dao)
        self.controller = MovieController(self.service)
        self.view = MovieView()

    def test_add_movie(self):
        # Simulate user entering movie details
        user_inputs = [
            "Inception", "Sci-Fi", "English",
            "148", "2026-01-01", "2026-12-31"
        ]

        with patch("builtins.input", side_effect=user_inputs):#mentioned in notepad that thisis for return inputs like manual user
            with patch("builtins.print") as mock_print:#after sucess it print like normal print
                self.view.add_movie(self.controller)

        # Check that the movie was saved
        connection = sqlite3.connect(self.db_path)
        movie = connection.execute(
            "SELECT movie_title FROM movie"
        ).fetchone()
        connection.close()

        self.assertEqual(movie[0], "Inception")
        mock_print.assert_any_call("Added Succesfull")
#test invalid date
    def test_add_movie_invalid_dates(self):
        user_inputs = [
            "Inception", "Sci-Fi", "English",
            "148", "2026-12-31", "2026-01-01"
        ]
        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_movie(self.controller)
        mock_print.assert_any_call(
            "Adding Failed or missmatch of dates are found!!!"
        )
#view_movie
    
    
    def test_update_movie(self):
    # First, add a movie to the database
        self.dao.add_movie(
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        )

        # Simulate the user's input for updating the movie
        user_inputs = [
            "1",             # Movie ID
            "Interstellar",  # New title
            "Sci-Fi",        # New genre
            "English",       # New language
            "169",           # New duration
            "2026-01-01",    # Release date
            "2026-12-31"     # End date
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.update_movie(self.controller)

        # Check whether the movie was updated
        movie = self.controller.search_movie(1)
        self.assertEqual(movie[1], "Interstellar")

        # Check the success message
        mock_print.assert_any_call("Updated Successfully")

    def test_delete_movie(self):
        # Add a movie first
        self.dao.add_movie(
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        )

        # Simulate the user's input
        user_inputs = ["1"]  # Movie ID to delete

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.delete_movie(self.controller)

        # Check whether the movie was deleted
        result = self.controller.search_movie(1)
        self.assertIsNone(result)

        # Check the success message
        mock_print.assert_any_call("Deleted Successfully")

    def test_search_movie(self):
        # Add a movie to the database
        self.dao.add_movie(
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        )
        # Enter the movie ID when the CLI asks
        user_inputs = ["1"]
        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.search_movie(self.controller)
        # Check whether the movie title was displayed
        mock_print.assert_any_call("Inception")
    #search not found
    def test_search_movie_not_found(self):
        user_inputs = ["999"]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.search_movie(self.controller)

        # Check that the CLI displays a not-found message
        mock_print.assert_any_call("Movie not found")
    #update invalid dates
    def test_update_movie_invalid_dates(self):
        # Add an existing movie
        self.dao.add_movie(
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        )

        # Enter updated details with invalid dates
        user_inputs = [
            "1",
            "Interstellar",
            "Sci-Fi",
            "English",
            "169",
            "2026-12-31",  # Release date
            "2026-01-01"   # End date
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.update_movie(self.controller)

        # Check that the original title remains unchanged
        movie = self.controller.search_movie(1)
        self.assertEqual(movie[1], "Inception")

        # Check the failure message
        mock_print.assert_any_call(
            "Adding Failed or missmatch of dates are found!!!"
        )

    #movie not found
    def test_delete_movie_not_found(self):
        # Enter a movie ID that does not exist
        user_inputs = ["999"]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.delete_movie(self.controller)

        # Check the message shown by the CLI
        mock_print.assert_any_call("Movie not found")
    #movie search but no movies in database
    def test_view_movie_empty(self):
        with patch("builtins.print") as mock_print:
            self.view.view_movie(self.controller)

        # Check whether the CLI displays a message
        mock_print.assert_any_call("No movies found")
    def tearDown(self):
        self.patcher.stop()
        os.remove(self.db_path)


if __name__ == "__main__":
    unittest.main()
