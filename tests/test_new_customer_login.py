#new customer save and finding
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestNewCustomerLogin(unittest.TestCase):
    def test_new_customer_login(self):
        mock_dao = Mock()
        mock_dao.save.return_value = 10
        service = BookingService(mock_dao)
        result = service.new_customer_login(9876543210)
        self.assertEqual(result, 10)
        mock_dao.save.assert_called_once_with(9876543210)

