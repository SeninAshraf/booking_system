#test admin login
import unittest
from unittest.mock import Mock
import bcrypt
from services.authenticationservice import AuthenticationService
class TestAdminLogin(unittest.TestCase):
    def test_admin_login_success(self):
        mock_dao = Mock()
        password_hash = bcrypt.hashpw(#converting pass to hash1. first convert fake pass to hash
            b"Admin123",
            bcrypt.gensalt()
        ).decode("utf-8")
        mock_admin = Mock()
        mock_admin.passwordHash = password_hash#5.compare admin pass to this pass generated here
        mock_dao.find_admin.return_value = mock_admin#4.in mockdao initialise find admin return mock admin

        service = AuthenticationService(mock_dao)#3. move to service method in and then mock_dao
        result = service.login_admin("admin", "Admin123")#2. call the function
        self.assertTrue(result)#6.chehck result get true
        mock_dao.find_admin.assert_called_once_with("admin")#7.also ensure it only gotten 1 time
