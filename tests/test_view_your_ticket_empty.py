#view your tickets when when the customer has no tickets.
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestViewYourTicketsEmpty(unittest.TestCase):
    def test_no_tickets(self):
        mock_dao = Mock()
        mock_dao.view_your_tickets.return_value = []

        service = BookingService(mock_dao)
        result = service.view_your_tickets(9876543210)

        self.assertIsNone(result)
        mock_dao.view_your_tickets.assert_called_once_with(9876543210)



