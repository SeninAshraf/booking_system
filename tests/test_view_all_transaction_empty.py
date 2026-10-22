#test when there are no booking transactions
import unittest
from unittest.mock import Mock
from services.reportingservice import ReportingService
class TestViewAllEmpty(unittest.TestCase):
    def test_view_all_teransaction_empty(self):
        mock_booking_dao= Mock()
        mock_booking_dao.view_all_transaction.return_value = None
        services = ReportingService(mock_booking_dao)
        result = services.view_all_transaction()
        self.assertIsNone(result,[])
        mock_booking_dao.view_all_transaction.assert_called_once()