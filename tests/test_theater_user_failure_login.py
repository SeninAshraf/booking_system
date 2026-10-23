#test theater failure login
import unittest
from unittest.mock import Mock
import bcrypt
from services.authenticationservice import AuthenticationService
class TestTheaterUserLoginFailure(unittest.TestCase):
    def test_wrong_password(self):
        mock_dao = Mock()
        password_hash = bcrypt.hashpw(
            b"Theater123",
            bcrypt.gensalt()
        ).decode("utf-8")
        mock_user = Mock()
        mock_user.passwordHash = password_hash
        mock_user.firstLogin = False
        mock_dao.find_theater_user.return_value = mock_user
        service = AuthenticationService(mock_dao)
        result = service.login_user(
            "Grand Cinema", "grand_admin", "Wrong123"
        )
        self.assertFalse(result)
        mock_dao.find_theater_user.assert_called_once_with("Grand Cinema")