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