# Test whether booking is allowed when available seats equal requested tickets.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatReq(unittest.TestCase):
    def test_exact_number_of_seats_available(self):
        mock_dao = Mock()
        mock_dao.check_number_of_seats.return_value = 3
        service = SeatService(mock_dao)
        result = service.check_number_of_seats(1, 3)
        self.assertTrue(result)
        mock_dao.check_number_of_seats.assert_called_once_with(1)
