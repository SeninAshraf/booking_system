# Test whether view_show_based_theater returns shows for the selected theater and movie.
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class TestShowsCollision(unittest.TestCase):
    def test_view_show_based_theater(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        expected_shows = [
            (1, "10:00", "12:00"),
            (2, "14:00", "16:00")
        ]

        mock_show_dao.view_show_based_theater.return_value = expected_shows

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.view_show_based_theater(1, 2)

        self.assertEqual(result, expected_shows)

        mock_show_dao.view_show_based_theater.assert_called_once_with(1, 2)
