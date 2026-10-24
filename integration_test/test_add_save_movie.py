import unittest
import sqlite3
import tempfile
import os#close the temp data
from unittest.mock import patch #for diverting the dao to temp data from org data

from dao.moviedao import MovieDao   #for testing wheather they work together this is real data
from services.movieservice import MovieService

class TestMovieIntegration(unittest.TestCase):#test class
    pass