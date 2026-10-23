# Test whether add_seats returns True without calling the DAO when zero seats are requested.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatZeroConfigure(unittest.TestCase):
    def test_add_zero_seats(self):
        mock_dao = Mock()
        service = SeatService(mock_dao)

        result = service.add_seats(
                1,    # show_id
                0,    # vip_rows
                0,    # vip_number_of_seats_per_row
                500,  # ticket_price_vip
                0,    # economy_rows
                0,    # economy_number_of_seats_per_row
                200   # ticket_price_economy
            )

        self.assertTrue(result)
        mock_dao.add_seat.assert_not_called()
