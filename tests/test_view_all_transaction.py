import unittest
from unittest.mock import Mock
from services.reportingservice import ReportingService
class TestViewAll(unittest.TestCase):
    def test_view_all_transaction(self):
        mock_booking_dao= Mock()
        mock_booking_dao.view_all_transaction.return_value = [
            (1, 9876543210, "Leo", 101, "A1", 500, "Booked")
        ]
        services = ReportingService(mock_booking_dao)
        result = services.view_all_transaction()
        self.assertTrue(result)
        mock_booking_dao.view_all_transaction.assert_called_once()