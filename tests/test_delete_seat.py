#if user enter show_id 1 check is it called on in dao
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatDelete(unittest.TestCase):
    def test_seat_delete(self):
        mock_dao=Mock()
        mock_dao.delete_seats.return_value = True
        service = SeatService(mock_dao)
        result = service.delete_seat(1)
        self.assertTrue(result)
        mock_dao.delete_seats.assert_called_once_with(1)
