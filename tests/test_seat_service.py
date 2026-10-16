
import unittest
from unittest.mock import Mock, call
from services.seatservice import SeatService
class TestSeatService(unittest.TestCase):

    def test_add_seats(self):
        # Create a fake DAO
        mock_dao = Mock()
        service = SeatService(mock_dao)

        result = service.add_seats(
            1,  # show_id =1
            2,  # VIP rows = 2
            3,  # VIP seats per row=3
            500,  # VIP ticket price
            1,  # Economy rows = 1
            2,  # Economy seats per row =2
            200  # Economy ticket price =200
        )

        # is success
        self.assertTrue(result)

        # is 8 seat generated
        self.assertEqual(mock_dao.add_seat.call_count, 8)

        # is 1st is vip
        mock_dao.add_seat.assert_any_call(
            1, "A1", "VIP", "Available", 500, "A"
        )

        # is first is economy
        mock_dao.add_seat.assert_any_call(
            1, "C1", "Economy", "Available", 200, "C"
        )


if __name__ == "__main__":
    unittest.main()
