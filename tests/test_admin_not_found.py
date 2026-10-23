#test for user didnt exist
import unittest
from unittest.mock import Mock
from services.authenticationservice import AuthenticationService
class TestAdminNotFound(unittest.TestCase):
    def test_admin_not_found(self):
        mock_dao = Mock()
        mock_dao.find_admin.return_value = None
        service = AuthenticationService(mock_dao)
        result = service.login_admin("unknown_admin", "Admin123")
        self.assertFalse(result)
        mock_dao.find_admin.assert_called_once_with("unknown_admin")
