#successful customer login when the customer already exists.
import unittest
from unittest.mock import Mock
from services.authenticationservice import AuthenticationService
class TestExistingCustomer(unittest.TestCase):
    def test_existing_customer(self):
        mock_auth_dao = Mock()
        mock_auth_dao.find_customer.return_value = (1, 9876543210)
        service = AuthenticationService(mock_auth_dao)
        result = service.login_customer(9876543210)
        self.assertEqual(result, (1, 9876543210))
        mock_auth_dao.find_customer.assert_called_once_with(9876543210)

