# Test whether add_seats returns True without calling the DAO when zero seats are requested.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatZeroConfigure(unittest.TestCase):
    def test_add_zero_seats(self):
        mock_dao = Mock()
        service = SeatService(mock_dao)

        result = service.add_seats(
            1, 0, 0, 500,
            0, 0, 200
        )

        self.assertTrue(result)
        mock_dao.add_seat.assert_not_called()
