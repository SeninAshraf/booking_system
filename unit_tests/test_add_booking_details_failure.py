#failure of add booking details whenwhen the DAO fails to create a bookin
import unittest
from unittest.mock import Mock
from services.bookingservice import BookingService
class TestAddBookingDetailsFailure(unittest.TestCase):
    def test_add_booking_details_failure(self):
        mock_dao = Mock()
        mock_dao.add_booking_details.return_value = False
        service = BookingService(mock_dao)
        result = service.add_booking_details(1, 10, 400, 2)
        self.assertFalse(result)
        mock_dao.add_booking_details.assert_called_once_with(
            1, 10, 400, 2
        )