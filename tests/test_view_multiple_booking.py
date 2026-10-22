#test wheather it handle multiple seat in same booking
import unittest
from unittest.mock import Mock
from services.reportingservice import ReportingService
class TestMultipleBookingSeats(unittest.TestCase):
    def test_multiple_seats(self):
        mock_dao = Mock()
        mock_dao.view_all_transaction.return_value = [
            (1, 9876543210, "Leo", 101, "A1", 500, "Booked"),
            (1, 9876543210, "Leo", 101, "A2", 500, "Booked")
        ]
        service = ReportingService(mock_dao)
        service.view_all_transaction()
        mock_dao.view_all_transaction.assert_called_once()
