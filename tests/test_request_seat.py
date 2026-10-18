import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatReq(unittest.TestCase):
    def test_not_enough_seats(self):
        mock_dao = Mock()
        mock_dao.check_number_of_seats.return_value = 2

        service = SeatService(mock_dao)

        result = service.check_number_of_seats(1, 3)

        self.assertFalse(result)