import unittest
from unittest.mock import Mock
from services.showservice import ShowService
class TestSearchService(unittest.TestCase):
    def test_search_show_not_found(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        mock_show_dao.search_show.return_value = None

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.search_show(999)

        self.assertIsNone(result)

        mock_show_dao.search_show.assert_called_once_with(999)
