# Test whether the service handles an empty seat list when no seats are found.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class TestEmptySeat(unittest.TestCase):
    def test_view_seat_based_shows_no_seats(self):
        mock_dao = Mock()
        mock_dao.view_seat_based_shows.return_value = []

        service = SeatService(mock_dao)

        result = service.view_seat_based_shows(1)

        self.assertIsNone(result)
        mock_dao.view_seat_based_shows.assert_called_once_with(1)
