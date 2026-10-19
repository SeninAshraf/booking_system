# Test whether the service returns the correct seat records, seat numbers, and booking statuses
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class TestSeatbasedShows(unittest.TestCase):

    def test_view_seat_based_shows(self):
        mock_dao = Mock()

        mock_dao.view_seat_based_shows.return_value = [
            (1, 1, "A1", "VIP", "Available", 500, "A"),
            (2, 1, "A2", "VIP", "Booked", 500, "A"),
        ]
        service = SeatService(mock_dao)
        result = service.view_seat_based_shows(1)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][2], "A1")
        self.assertEqual(result[1][4], "Booked")
        mock_dao.view_seat_based_shows.assert_called_once_with(1)
