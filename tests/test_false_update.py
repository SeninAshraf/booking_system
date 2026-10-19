#If the DAO returns False, does the service return False too?
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatDeleteFalse(unittest.TestCase):
    def test_delete_seat_failure(self):
        mock_dao = Mock()
        mock_dao.delete_seats.return_value = False

        service = SeatService(mock_dao)

        result = service.delete_seat(1)

        self.assertFalse(result)
        mock_dao.delete_seats.assert_called_once_with(1)
