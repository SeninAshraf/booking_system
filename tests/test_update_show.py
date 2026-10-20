# Test whether update_show passes the updated show details to the DAO and returns its result.
import unittest
from unittest.mock import Mock
from services.showservice import ShowService
class TestUpdateShow(unittest.TestCase):
    def test_update_show(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()
        mock_show_dao.update_show.return_value = True
        service = ShowService(mock_show_dao, mock_movie_dao)
        result = service.update_show(
            1, 2, "2026-10-25", "10:00", "12:00"
        )
        self.assertTrue(result)
        mock_show_dao.update_show.assert_called_once_with(
            1, 2, "2026-10-25", "10:00", "12:00"
        )