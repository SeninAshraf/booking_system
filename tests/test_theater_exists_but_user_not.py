# Test that a user can be registered for an existing theater without creating another theater.
import bcrypt
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService
class TestExistingTheater(unittest.TestCase):
    def test_add_user_to_existing_theater(self):
        mock_theater_dao = Mock()
        mock_official_dao = Mock()
        mock_theater_dao.get_theater.return_value = (5, "Grand Cinema")#from serching theater it retruns id and name of theater
        mock_official_dao.find_theater_user.return_value = None#checking theater_user and didnt found
        mock_official_dao.add_theateruser.return_value = True#so theater exist but no user so system call add_theater method from dao and returns true
        service = TheaterofficialService(
            mock_theater_dao,
            mock_official_dao
        )
        result = service.add_theater_user(#step 1 of getting arguments 3
            "Grand Cinema",
            "grand_admin",
            "SecurePass123"
        )
        self.assertTrue(result)#check is result true
        mock_theater_dao.add_theater.assert_not_called()#check add_theater not called
        mock_official_dao.find_theater_user.assert_called_once_with(5)#check it once called find_theater_user
        mock_official_dao.add_theateruser.assert_called_once()#check it called add theater_user (in inside service code it has 3 arguments)
        saved_args = mock_official_dao.add_theateruser.call_args.args#3 arguments(theater_id,username and pass saved) 
        self.assertEqual(saved_args[0], 5)#compare
        self.assertEqual(saved_args[1], "grand_admin")#compare
        self.assertNotEqual(saved_args[2], "SecurePass123")#compare then hashing occur

        self.assertTrue(
            bcrypt.checkpw(
                b"SecurePass123",
                saved_args[2].encode("utf-8")
            )
        )
        
        
        
