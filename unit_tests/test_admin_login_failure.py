#test wheather admin has try to login using incorrect pass
import unittest
from unittest.mock import Mock
import bcrypt
from services.authenticationservice import AuthenticationService
class TestAdminLoginFailure(unittest.TestCase):
    def test_admin_login_wrong_password(self):
        mock_dao = Mock()
        password_hash = bcrypt.hashpw(
            b"Admin123",
            bcrypt.gensalt()
        ).decode("utf-8")
        mock_admin = Mock()
        mock_admin.passwordHash = password_hash
        mock_dao.find_admin.return_value = mock_admin
        service = AuthenticationService(mock_dao)
        result = service.login_admin("admin", "Wrong123")
        self.assertFalse(result)
        mock_dao.find_admin.assert_called_once_with("admin")


#same workflow as test_admin_login