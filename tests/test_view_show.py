# Test whether view_show returns the shows for the given theater ID.
import unittest
from unittest.mock import Mock
from services.showservice import ShowService
class TestShowService(unittest.TestCase):
    def test_view_show(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()
        expected_shows = [
            (1, "10:00", "2026-10-20"),
            (2, "14:00", "2026-10-20")
        ]
        mock_show_dao.get_all.return_value = expected_shows
        service = ShowService(mock_show_dao, mock_movie_dao)
        result = service.view_show(1)
        print(result)
        self.assertEqual(result, expected_shows)
        mock_show_dao.get_all.assert_called_once_with(1)


