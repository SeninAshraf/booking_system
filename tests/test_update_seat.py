#check when updating seat status is that correct seat is call and received in dao and is it call by once
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class SeatUpdate(unittest.TestCase):

    def test_update_booked_seats(self):
        mock_dao = Mock()
        mock_dao.update_booked_seats.return_value = True

        service = SeatService(mock_dao)

        result = service.update_booked_seats(1, ["A1", "A2"])

        self.assertTrue(result)

        mock_dao.update_booked_seats.assert_called_once_with(
            1, ["A1", "A2"]
        )
