# Test whether delete_show passes the show ID to the DAO and returns its result.
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class ShowDelete(unittest.TestCase):
    def test_delete_show(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        mock_show_dao.delete_show.return_value = True

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.delete_show(1)

        self.assertTrue(result)
        mock_show_dao.delete_show.assert_called_once_with(1)
