import unittest
import sqlite3
import tempfile
import os
from unittest.mock import patch

from dao.moviedao import MovieDao
from services.movieservice import MovieService