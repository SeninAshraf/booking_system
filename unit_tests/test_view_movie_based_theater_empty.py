#Test when no theaters are available for the selected movie.
import unittest
from unittest.mock import Mock
from services.theaterservice import TheaterService
class TestViewTheaterBasedMovie(unittest.TestCase):
    def view_theater_based_movie(self):
        mock_theater_dao=Mock()
        mock_theater_dao.view_movie_based_theater.return_value = None
        service = TheaterService(mock_theater_dao)
        result=service.view_movie_based_theater(10)
        self.assertFalse(result)
        mock_theater_dao.view_movie_based_theater.assert_called_once_with(10)