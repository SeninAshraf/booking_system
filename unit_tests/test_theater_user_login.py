#test theater_login_2nd time
import unittest
from unittest.mock import Mock
import bcrypt
from services.authenticationservice import AuthenticationService
class TestTheaterUserLogin(unittest.TestCase):
    def test_theater_user_login_success(self):
        mock_dao = Mock()
        password_hash = bcrypt.hashpw(
            b"Theater123",
            bcrypt.gensalt()
        ).decode("utf-8")
        mock_user = Mock()
        mock_user.passwordHash = password_hash
        mock_user.firstLogin = False#no password reset
        mock_dao.find_theater_user.return_value = mock_user
        service = AuthenticationService(mock_dao)
        result = service.login_user(
            "Grand Cinema", "grand_admin", "Theater123"
        )
        self.assertEqual(result, mock_user)
        mock_dao.find_theater_user.assert_called_once_with("Grand Cinema")



