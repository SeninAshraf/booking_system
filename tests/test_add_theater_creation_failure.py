# Test that user registration stops when creating the theater fails.
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService
class TestTheaterCreationFailure(unittest.TestCase):
    def test_add_theater_user_theater_creation_fails(self):
        mock_theater_dao = Mock()
        mock_official_dao = Mock()
        mock_theater_dao.get_theater.return_value = None#tHEATER DOES NOT EXIST SO IT GO TO ADD THEATER
        mock_theater_dao.add_theater.return_value = None#but unexpectaedly theater creation failed and return none
        service = TheaterofficialService(
            mock_theater_dao,
            mock_official_dao
        )
        result = service.add_theater_user(
            "Grand Cinema",
            "grand_admin",
            "SecurePass123"
        )
        self.assertFalse(result)
        mock_theater_dao.get_theater.assert_called_once_with(#searching theater once happen
            "Grand Cinema"
        )
        mock_theater_dao.add_theater.assert_called_once_with(#add theater method also called at once but it retrun none
            "Grand Cinema"
        )
        mock_official_dao.find_theater_user.assert_not_called()#so no calling of find theater
        mock_official_dao.add_theateruser.assert_not_called()#nothing happen



