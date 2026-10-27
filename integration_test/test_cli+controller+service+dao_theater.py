
import unittest
import sqlite3
import tempfile
import bcrypt
import os
from unittest.mock import patch

from dao.theaterdao import TheaterDao
from dao.theaterofficialdao import TheaterOfficialDao
from services.theaterservice import TheaterService
from services.theaterofficialservice import TheaterofficialService
from controllers.theaterofficialcontroller import TheaterofficialController
from view.cliview import MovieView


class TestTheaterIntegration(unittest.TestCase):

    def setUp(self):
        # Create a temporary database
        fd, self.db_path = tempfile.mkstemp()
        os.close(fd)

        connection = sqlite3.connect(self.db_path)

        connection.executescript("""
            CREATE TABLE theater (
                theater_id INTEGER PRIMARY KEY AUTOINCREMENT,
                theater_name TEXT UNIQUE
            );

            CREATE TABLE theater_user (
                theater_id INTEGER PRIMARY KEY,
                username TEXT,
                password_hash TEXT,
                require_password_reset INTEGER
            );
        """)

        connection.close()

        # Redirect both DAOs to the temporary database
        def create_connection():
            return sqlite3.connect(self.db_path)

        self.patcher1 = patch(
            "dao.theaterdao.get_connection",
            side_effect=create_connection
        )
        self.patcher1.start()
        
        self.patcher2 = patch(
            "dao.theaterofficialdao.get_connection",
             side_effect=create_connection
        )
        self.patcher2.start()

        # Create the objects
        self.theater_dao = TheaterDao()
        self.theater_official_dao = TheaterOfficialDao()

        self.theater_service = TheaterService(self.theater_dao)

        self.theater_official_service = TheaterofficialService(
            self.theater_dao,
            self.theater_official_dao
        )

        self.controller = TheaterofficialController(
            self.theater_official_service,
            self.theater_service
        )

        self.view = MovieView()

    def test_add_theater_user(self):
        user_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_theater_user(self.controller)

        # Check the success message
        mock_print.assert_any_call(
            "Theater user added succesfully."
        )

        # Check that the theater was saved
        connection = sqlite3.connect(self.db_path)

        theater = connection.execute(
            "SELECT theater_name FROM theater"
        ).fetchone()

        # Check that the theater user was saved
        theater_user = connection.execute(
            "SELECT theater_id, username, password_hash "
            "FROM theater_user"
        ).fetchone()

        connection.close()

        self.assertEqual(theater[0], "Grand Cinema")
        self.assertEqual(theater_user[1], "grand_admin")

        # Check that the password is hashed, not stored as plain text
        self.assertNotEqual(theater_user[2], "test123")

    def test_duplicate_theater_user(self):
    # Register the first theater user
        first_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=first_inputs):
            with patch("builtins.print"):
                self.view.add_theater_user(self.controller)

        # Try to register another user for the same theater
        second_inputs = [
            "Grand Cinema",
            "another_admin",
            "test456"
        ]

        with patch("builtins.input", side_effect=second_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_theater_user(self.controller)

        # Check the failure message
        mock_print.assert_any_call("user addition failed.")

        # Check that only one theater user exists
        connection = sqlite3.connect(self.db_path)

        result = connection.execute(
            "SELECT COUNT(*) FROM theater_user"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(result, 1)

    #test registering users for two different theaters. This verifies that your application creates separate theater records and user accounts.
    def test_add_users_for_different_theaters(self):
    # Register the first theater
        first_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=first_inputs):
            with patch("builtins.print"):
                self.view.add_theater_user(self.controller)

        # Register the second theater
        second_inputs = [
            "City Cinema",
            "city_admin",
            "test456"
        ]

        with patch("builtins.input", side_effect=second_inputs):
            with patch("builtins.print"):
                self.view.add_theater_user(self.controller)

        # Check the number of theaters and users
        connection = sqlite3.connect(self.db_path)

        theater_count = connection.execute(
            "SELECT COUNT(*) FROM theater"
        ).fetchone()[0]

        user_count = connection.execute(
            "SELECT COUNT(*) FROM theater_user"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(theater_count, 2)
        self.assertEqual(user_count, 2)
#case sensitive
    def test_theater_name_case_insensitive(self):
        # Register the first user
        first_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=first_inputs):
            with patch("builtins.print"):
                self.view.add_theater_user(self.controller)

        # Try registering with the same theater name in lowercase
        second_inputs = [
            "grand cinema",
            "another_admin",
            "test456"
        ]

        with patch("builtins.input", side_effect=second_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_theater_user(self.controller)

        # The second registration should fail
        mock_print.assert_any_call("user addition failed.")

        # Confirm only one theater was created
        connection = sqlite3.connect(self.db_path)

        count = connection.execute(
            "SELECT COUNT(*) FROM theater"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(count, 1)

    #correctly hashed using bcrypt
    def test_password_is_hashed_correctly(self):
        user_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print"):
                self.view.add_theater_user(self.controller)

        # Get the saved password hash
        connection = sqlite3.connect(self.db_path)

        result = connection.execute(
            "SELECT password_hash FROM theater_user"
        ).fetchone()

        connection.close()

        password_hash = result[0]

        # Check the original password against the stored hash
        self.assertTrue(
            bcrypt.checkpw(
                "test123".encode("utf-8"),
                password_hash.encode("utf-8")
            )
        )

    #test whether your CLI rejects missing input.
    def test_add_theater_user_empty_name(self):
        user_inputs = [
            "",             # Empty theater name
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_theater_user(self.controller)

        # Check the validation message
        mock_print.assert_any_call("All fields are required.")

        # Check that no theater was created
        connection = sqlite3.connect(self.db_path)

        count = connection.execute(
            "SELECT COUNT(*) FROM theater"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(count, 0)
    #registering a user for a theater that already exists but has no registered user yet.
    def test_add_user_to_existing_theater(self):
        # Create the theater without registering a user
        self.theater_dao.add_theater("Grand Cinema")

        # Register a user for the existing theater
        user_inputs = [
            "Grand Cinema",
            "grand_admin",
            "test123"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            with patch("builtins.print") as mock_print:
                self.view.add_theater_user(self.controller)

        # Check the success message
        mock_print.assert_any_call(
            "Theater user added succesfully."
        )

        # Check that no duplicate theater was created
        connection = sqlite3.connect(self.db_path)

        theater_count = connection.execute(
            "SELECT COUNT(*) FROM theater"
        ).fetchone()[0]

        user_count = connection.execute(
            "SELECT COUNT(*) FROM theater_user"
        ).fetchone()[0]

        connection.close()

        self.assertEqual(theater_count, 1)
        self.assertEqual(user_count, 1)

    def test_view_theaters(self):
        # Add theaters to the temporary database
        self.theater_dao.add_theater("Grand Cinema")
        self.theater_dao.add_theater("City Cinema")

        # Call the controller to retrieve theaters
        result = self.controller.view_theaters()

        # Check the retrieved theaters
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][1], "Grand Cinema")
        self.assertEqual(result[1][1], "City Cinema")
    def test_view_theaters_empty(self):
        # Retrieve theaters from the empty database
        result = self.controller.view_theaters()
        # Check that no theaters are returned
        self.assertEqual(result, [])
    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        os.remove(self.db_path)


if __name__ == "__main__":
    unittest.main()
