# Test that registration is rejected when the theater already has an official user.
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService
class TestTheaterUserExists(unittest.TestCase):
    def test_add_theater_user_already_exists(self):
        mock_theater_dao = Mock()
        mock_official_dao = Mock()
        
        mock_theater_dao.get_theater.return_value = (1, "Grand Cinema")#it already have  theater 

        
        mock_official_dao.find_theater_user.return_value = (
            1, "grand_admin"#already have user also
        )

        service = TheaterofficialService(
            mock_theater_dao,
            mock_official_dao
        )

        result = service.add_theater_user(
            "Grand Cinema",
            "another_admin",
            "SecurePass123"
        )

        self.assertFalse(result)#chechk if it return the false

        mock_theater_dao.get_theater.assert_called_once_with(
            "Grand Cinema"#check it only called once
        )
        mock_theater_dao.add_theater.assert_not_called()#chehck add_theater not called
        mock_official_dao.find_theater_user.assert_called_once_with(1)#check find_theater_username once
        mock_official_dao.add_theateruser.assert_not_called()#no call add_theatre user
