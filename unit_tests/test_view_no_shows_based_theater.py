# Test that an empty list is returned when no shows are available.
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class TestShowsCollision(unittest.TestCase):
    def test_view_show_based_theater_no_shows(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        mock_show_dao.view_show_based_theater.return_value = []

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.view_show_based_theater(1, 2)

        self.assertEqual(result, [])

        mock_show_dao.view_show_based_theater.assert_called_once_with(1, 2)
