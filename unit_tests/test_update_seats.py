# Test whether existing seats are deleted and the new seat layout is generated correctly.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatUpdateNew(unittest.TestCase):
    def test_update_seats(self):
        mock_dao = Mock()
        service = SeatService(mock_dao)

        result = service.update_seats(
            1,  # show_id
            1,  # VIP rows
            2,  # VIP seats per row
            500,  # VIP price
            1,  # Economy rows
            2,  # Economy seats per row
            200   # Economy price
        )

        self.assertTrue(result)
        mock_dao.delete_seats.assert_called_once_with(1)
        self.assertEqual(mock_dao.add_seat.call_count, 4)#4 seat added(4 times add_seat method were called)
