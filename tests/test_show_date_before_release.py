# Test that a show cannot be created before the movie's release date.
from datetime import datetime , date
import unittest
from unittest.mock import Mock, call
from services.showservice import ShowService
class TestShowsCollision(unittest.TestCase):
    def test_add_show_before_release_date(self):
        mock_show_dao = Mock()
        mock_movie_dao = Mock()

        mock_movie_dao.get_movie.return_value = (
            1, "Movie A", "Action", "English", 120,
            "2026-10-15", "2026-11-30"
        )

        service = ShowService(mock_show_dao, mock_movie_dao)

        result = service.add_show(
            1,
            1,
            1,
            date(2026, 10, 10),
            datetime.strptime("10:00", "%H:%M").time(),
            datetime.strptime("12:00", "%H:%M").time()
        )

        self.assertIsNone(result)
        mock_show_dao.check_show_collision.assert_not_called()
        mock_show_dao.add_show.assert_not_called()