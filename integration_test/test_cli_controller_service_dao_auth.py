import unittest
import sqlite3
import tempfile
import os
import bcrypt
from unittest.mock import patch

from dao.authenticationdao import AuthDao
from services.authenticationservice import AuthenticationService


class TestAuthenticationIntegration(unittest.TestCase):

    def setUp(self):
        fd, self.db_path = tempfile.mkstemp()
        os.close(fd)

        connection = sqlite3.connect(self.db_path)

        connection.executescript("""
            CREATE TABLE admin (
                admin_username TEXT UNIQUE,
                password_hash TEXT
            );

            CREATE TABLE theater (
                theater_id INTEGER PRIMARY KEY,
                theater_name TEXT UNIQUE
            );

            CREATE TABLE theater_user (
                theater_user_id INTEGER PRIMARY KEY,
                theater_id INTEGER,
                username TEXT UNIQUE,
                password_hash TEXT,
                require_password_reset BOOLEAN,
                FOREIGN KEY (theater_id)
                    REFERENCES theater(theater_id)
            );

            CREATE TABLE customer (
                customer_id INTEGER PRIMARY KEY,
                mobile_number CHAR UNIQUE
            );
        """)

        password_hash = bcrypt.hashpw(
            b"admin123",
            bcrypt.gensalt()
        ).decode("utf-8")

        connection.execute(
            "INSERT INTO admin VALUES (?, ?)",
            ("admin", password_hash)
        )

        connection.commit()
        connection.close()

        self.patcher = patch(
            "dao.authenticationdao.get_connection",
            side_effect=self.connect_test_db
        )
        self.patcher.start()

        self.auth_dao = AuthDao()
        self.auth_service = AuthenticationService(self.auth_dao)

    def connect_test_db(self):
        return sqlite3.connect(self.db_path)

    def tearDown(self):
        self.patcher.stop()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_admin_login_success(self):
        result = self.auth_service.login_admin(
            "admin",
            "admin123"
        )

        self.assertTrue(result)

    def test_admin_login_wrong_password(self):
        result = self.auth_service.login_admin(
            "admin",
            "wrongpassword"
        )

        self.assertFalse(result)

    def test_admin_login_unknown_username(self):
        result = self.auth_service.login_admin(
            "unknown",
            "admin123"
        )

        self.assertFalse(result)


