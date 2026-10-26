
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

    def tearDown(self):
        self.patcher.stop()
        os.remove(self.db_path)


if __name__ == "__main__":
    unittest.main()
