#test theater user not found
import unittest
from unittest.mock import Mock
from services.authenticationservice import AuthenticationService
class TestTheaterUserNotFound(unittest.TestCase):
    def test_theater_user_not_found(self):
        mock_dao = Mock()
        mock_dao.find_theater_user.return_value = None
        service = AuthenticationService(mock_dao)
        result = service.login_user(
            "Grand Cinema", "grand_admin", "Theater123"
        )
        self.assertFalse(result)
        mock_dao.find_theater_user.assert_called_once_with("Grand Cinema")