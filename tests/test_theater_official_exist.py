# Test that check_user returns the official user details for the given theater ID.
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService
class TestTheaterCheckUser(unittest.TestCase):
    def test_check_user_exists(self):
        mock_theater_dao = Mock()
        mock_official_dao = Mock()
        expected_user = (1, "grand_admin", "hashed_password")#existing user details
        mock_official_dao.find_theater_user.return_value = expected_user#when user check the find_theater_user it returns details of existing user
        service = TheaterofficialService(
            mock_theater_dao,#initialise the service method
            mock_official_dao
        )
        result = service.check_user(1)#check the user with theater_id
        self.assertEqual(result, expected_user)#compare the result with expected user
        mock_official_dao.find_theater_user.assert_called_once_with(1)
