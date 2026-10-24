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
       os.close(fd)