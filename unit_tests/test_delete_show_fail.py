# Test that delete_show returns False when the DAO deletion fails.
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class ShowDelete(unittest.TestCase):
    def test_delete_show_failure(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()
        mock_show_dao.delete_show.return_value = False
        service = ShowService(mock_show_dao, mock_movie_dao)
        result = service.delete_show(999)
        self.assertFalse(result)
        mock_show_dao.delete_show.assert_called_once_with(999)
