#test add booking details
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestAddBookingDetails(unittest.TestCase):
    def test_add_booking_details(self):
        mock_dao = Mock()
        mock_dao.add_booking_details.return_value = 100
        service = BookingService(mock_dao)
        result = service.add_booking_details(1, 10, 400, 2)
        self.assertEqual(result, 100)
        mock_dao.add_booking_details.assert_called_once_with(
            1, 10, 400, 2
        )


