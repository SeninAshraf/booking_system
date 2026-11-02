#test when new customer failure
import unittest
from unittest.mock import Mock
from services.authenticationservice import AuthenticationService
class TestNewCustomerLoginFailure(unittest.TestCase):
    def test_new_customer_login_failure(self):
        mock_dao = Mock()
        mock_dao.save.return_value = False
        service = AuthenticationService(mock_dao)
        result = service.new_customer_login(9876543210)
        self.assertFalse(result)
        mock_dao.save.assert_called_once_with(9876543210)