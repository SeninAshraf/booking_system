from datetime import datetime , date
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class TestShowsCollision(unittest.TestCase):
    def test_add_show_collision(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        mock_movie_dao.get_movie.return_value = (
            1, "Movie A", "Action", "English", 120,
            "2026-10-01", "2026-11-30"
        )

        # there is an same show in sql.so it return true value
        mock_show_dao.check_show_collision.return_value = True

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.add_show(
            1,
            1,
            1,
            date(2026, 10, 25),
            datetime.strptime("10:00", "%H:%M").time(),
            datetime.strptime("12:00", "%H:%M").time()
        )

        self.assertIsNone(result)

        mock_show_dao.check_show_collision.assert_called_once_with(
            1, 1, "2026-10-25", "10:00", "12:00"
        )
        mock_show_dao.add_show.assert_not_called()
