#test admin login
import unittest
from unittest.mock import Mock
import bcrypt
from services.authenticationservice import AuthenticationService
class TestAdminLogin(unittest.TestCase):
    def test_admin_login_success(self):
        mock_dao = Mock()
        password_hash = bcrypt.hashpw(#converting pass to hash
            b"Admin123",
            bcrypt.gensalt()
        ).decode("utf-8")
        mock_admin = Mock()
        mock_admin.passwordHash = password_hash
        mock_dao.find_admin.return_value = mock_admin

        service = AuthenticationService(mock_dao)
        result = service.login_admin("admin", "Admin123")
        self.assertTrue(result)
        mock_dao.find_admin.assert_called_once_with("admin")
