#test new login of theater user
import unittest
from unittest.mock import Mock
from services.authenticationservice import AuthenticationService


class TestUpdatePassword(unittest.TestCase):

    def test_update_password(self):
        mock_dao = Mock()
        service = AuthenticationService(mock_dao)
        result = service.update_password("Grand Cinema", "grand_admin")
#it will prompt enter new pass from auth service then user input new pass then test pass
        self.assertTrue(result)
        mock_dao.changing_password.assert_called_once()

