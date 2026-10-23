#test for view theaters 
import unittest
from unittest.mock import Mock
from services.theaterservice import TheaterService
class TestTheaterService(unittest.TestCase):
    def test_view_theaters(self):
        mock_theater_dao = Mock()
        expected_theaters = [
            (1, "Grand Cinema"),#these are expected result in mock database
            (2, "City Cinemas")
        ]
        mock_theater_dao.view_theaters.return_value = expected_theaters#initialise mock_theater_dao as result is expected result
        service = TheaterService(mock_theater_dao)
        result = service.view_theaters()#call view service methos in service class
        self.assertEqual(result, expected_theaters)#compare the result and expected theaters
        mock_theater_dao.view_theaters.assert_called_once_with()#ensure it only call once