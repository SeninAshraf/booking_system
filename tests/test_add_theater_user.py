import bcrypt
import unittest
from unittest.mock import Mock
from services.theaterofficialservice import TheaterofficialService

class TestTheaterUserAdd(unittest.TestCase):
    def test_add_theater_user_success(self):
        mock_theater_dao = Mock() # mock theater dao
        mock_official_dao = Mock() #mock officiial dao


        mock_theater_dao.get_theater.return_value = None #no theater found
        mock_theater_dao.add_theater.return_value = 1#so create it and return 1 as theater id

        # No user is registered for this theater.
        mock_official_dao.find_theater_user.return_value = None #search any user exixting there and retrun none
        mock_official_dao.add_theateruser.return_value = True # new user create it

        service = TheaterofficialService(#method of service with 2 daos
            mock_theater_dao,
            mock_official_dao
        )

        result = service.add_theater_user(
            "Grand Cinema",   # extract add theater_user method and pass 3 values call the function
            "grand_admin",
            "SecurePass123"
        )

        self.assertTrue(result) # check it retruns true

        mock_theater_dao.get_theater.assert_called_once_with( #for searching any of same theater name existed it already returns none in line 12
            "Grand Cinema"
        )
        mock_theater_dao.add_theater.assert_called_once_with(# then call add_theater adn pass grand cinima
            "Grand Cinema"
        )
        mock_official_dao.find_theater_user.assert_called_once_with(1)#check if same id theater has username  and retrunrs none
        mock_official_dao.add_theateruser.assert_called_once() #so add theater usr called by once 

        # Verify the stored password is hashed, not plaintext.
        saved_args = mock_official_dao.add_theateruser.call_args.args #for extarcting each positional arguments value
        self.assertEqual(saved_args[0], 1)
        self.assertEqual(saved_args[1], "grand_admin")
        self.assertNotEqual(saved_args[2], "SecurePass123")#not equal
        self.assertTrue(bcrypt.checkpw(
               b"SecurePass123",
            saved_args[2].encode("utf-8")#checks whether the original password matches the stored hash.
                    )
            )

