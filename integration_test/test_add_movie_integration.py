
import unittest
import sqlite3
import os#for creating temperory database and close that database


class TestMovieIntegration(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")#temperory database sql
        self.connection.execute("""
            CREATE TABLE movie (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_title TEXT,
                movie_genre TEXT,
                movie_language TEXT,
                movie_duration INTEGER,
                release_date TEXT,
                end_date TEXT
            )
        """)#create a temperory database table movie

    def test_add_movie(self):
        self.connection.execute("""
            INSERT INTO movie (
                movie_title, movie_genre, movie_language,
                movie_duration, release_date, end_date
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        ))#add movie details in that table

        result = self.connection.execute(
            "SELECT movie_title FROM movie"
        ).fetchone()#check is that added

        self.assertEqual(result[0], "Inception")#check 1st value with inception

    def tearDown(self):
        self.connection.close()#close the database

