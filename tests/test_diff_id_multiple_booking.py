#test multiple bookings with different booking id
import unittest
from unittest.mock import Mock
from services.reportingservice import ReportingService
class TestMultipleBookings(unittest.TestCase):
    def test_multiple_bookings(self):
        mock_dao = Mock()
        mock_dao.view_all_transaction.return_value = [
            (1, 9876543210, "Leo", 101, "A1", 500, "Booked"),
            (2, 9123456780, "Interstellar", 102, "B1", 300, "Booked")
        ]
        service = ReportingService(mock_dao)
        service.view_all_transaction()
        mock_dao.view_all_transaction.assert_called_once()
