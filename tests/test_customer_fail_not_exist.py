#test when customer login fails because the customer does not exist.
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestCustomerLoginNotFound(unittest.TestCase):
    def test_customer_not_found(self):
        mock_dao = Mock()
        mock_dao.find_customer.return_value = None
        service = BookingService(mock_dao)
        result = service.login_customer(9876543210)
        self.assertIsNone(result)
        mock_dao.find_customer.assert_called_once_with(9876543210)
