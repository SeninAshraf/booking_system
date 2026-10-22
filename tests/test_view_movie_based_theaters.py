#test theater based on movie
import unittest
from unittest.mock import Mock
from services.theaterservice import TheaterService
class TestViewMovieBasedTheater(unittest.TestCase):
    def test_view_movie_based_theater(self):
        mock_theater_dao = Mock()#initialise mock dao
        expected_theaters = [
            (1, "Grand Cinema"),#mock result
            (2, "City Cinemas")
        ]
        mock_theater_dao.view_movie_based_theater.return_value = expected_theaters#initialise method result as expected result
        service = TheaterService(mock_theater_dao)#initialise service method
        result = service.view_movie_based_theater(10)#call service method result with id 10
        self.assertEqual(result, expected_theaters)#compare both are equal
        mock_theater_dao.view_movie_based_theater.assert_called_once_with(10)#ensure only once called.

