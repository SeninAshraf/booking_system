import unittest
import sqlite3
import tempfile
import os#close the temp data
from unittest.mock import patch #for diverting the dao to temp data from org data

from dao.moviedao import MovieDao   #for testing wheather they work together this is real data
from services.movieservice import MovieService

class TestMovieIntegration(unittest.TestCase):#test class
    def setUp(self):#setup test database
       fd, self.db_path = tempfile.mkstemp() #create a temp file fd+file descriptor,self.db_path=way to file
       os.close(fd)#tempfile.mkstemp() creates the file and gives us two things: fd and self.db_path and now we dont need fd
       connection = sqlite3.connect(self.db_path)#open temp database ,deb_path tells the way 
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
""")#create a movie table
       connection.close()
       #next most imp part patcher divert direction of dao > sqlite to dao> temp databse
       def create_connection():#creates a function.
            return sqlite3.connect(self.db_path)#return the " your temporary database.

       self.patcher = patch(
            "dao.moviedao.get_connection",#Find the get_connection function used inside dao/moviedao.py.,Temporarily replace its behavior.
            side_effect=create_connection#side_effect=create_connection means whenever the DAO calls get_connection(), Python runs create_connection() instead.
        )

       self.patcher.start()#Before this line, the replacement is prepared but not active. After this line, the DAO uses our create_connection() function.
# Use self to store the DAO object as an instance variable,
# so it can be accessed by all methods in this test class.
       self.dao = MovieDao()
       self.service = MovieService(self.dao)

    
    def test_search_movie(self):
        # Add a movie to the temporary database
        self.service.add_movie(
            "Inception", "Sci-Fi", "English",
            148, "2026-01-01", "2026-12-31"
        )

        # Search for the movie using ID 1
        result = self.service.search_movie(1)

        # Check whether the movie was found
        self.assertIsNotNone(result)

        # Check the movie title
        self.assertEqual(result[1], "Inception")
    def tearDown(self):#tearDown() runs after each test method, even if that test fails.It helps us clean up the resources used by the test.
                   self.patcher.stop()#Stops the patch and restores the DAO's original get_connection() function.
                   os.remove(self.db_path)
