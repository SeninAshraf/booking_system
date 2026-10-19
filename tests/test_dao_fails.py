#When the DAO returns False, the if condition is not satisfied. Your method reaches the end without a return statement, so Python automatically returns None.
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class TestSeatDaoFail(unittest.TestCase):

    def test_update_booked_seats_failure(self):
        mock_dao = Mock()
        mock_dao.update_booked_seats.return_value = False

        service = SeatService(mock_dao)

        result = service.update_booked_seats(1, ["A1", "A2"])

        self.assertIsNone(result)
        mock_dao.update_booked_seats.assert_called_once_with(
            1, ["A1", "A2"]
        )
