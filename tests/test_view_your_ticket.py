#test view your tickets when cutomer has tickets
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestViewYourTickets(unittest.TestCase):
    def test_view_your_tickets(self):
        mock_dao = Mock()
        mock_dao.view_your_tickets.return_value = [
            (1, "Leo", "A5", 400)
        ]
        service = BookingService(mock_dao)
        result = service.view_your_tickets(9876543210)
        self.assertTrue(result)
        mock_dao.view_your_tickets.assert_called_once_with(9876543210)


