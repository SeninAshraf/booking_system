# Test that check_user returns None when no official user exists.
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService

class TestTheaterCheckUserNotFound(unittest.TestCase):
    def test_check_user_not_found(self):
        mock_theater_dao = Mock()
        mock_official_dao = Mock()
        mock_official_dao.find_theater_user.return_value = None #after seraching the theater user with theater_id=999
        service = TheaterofficialService(
            mock_theater_dao,
            mock_official_dao
        )

        result = service.check_user(999)#chehck user with theater_id = 999

        self.assertIsNone(result)#ensure that result will be none
        mock_official_dao.find_theater_user.assert_called_once_with(999)#check that it only called in once


