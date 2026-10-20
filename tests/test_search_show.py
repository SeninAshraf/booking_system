# Test whether search_show returns the show details for the given show ID.
import unittest
from unittest.mock import Mock
from services.showservice import ShowService
class TestSearchService(unittest.TestCase):
    def test_search_show(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()
        expected_show = (1, 2, "2026-10-20", "10:00", "12:00")
        mock_show_dao.search_show.return_value = expected_show
        service = ShowService(mock_show_dao, mock_movie_dao)
        result = service.search_show(1)
        print(result)
        self.assertEqual(result, expected_show)
        mock_show_dao.search_show.assert_called_once_with(1)
