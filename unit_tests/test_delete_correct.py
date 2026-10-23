# Test whether seats are deleted for the given show ID and the DAO result is returned.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatDeleteCrct(unittest.TestCase):
    def test_delete_seat(self):
        mock_dao = Mock()
        mock_dao.delete_seats.return_value = True

        service = SeatService(mock_dao)

        result = service.delete_seat(1)

        self.assertTrue(result)
        mock_dao.delete_seats.assert_called_once_with(1)