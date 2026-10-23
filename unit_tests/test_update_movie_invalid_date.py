# Test that a movie cannot be updated when the end date precedes the release date.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieUpdateInvalidDate(unittest.TestCase):
    def test_update_movie_invalid_date(self):
        mock_movie_dao = Mock()
        service = MovieService(mock_movie_dao)
        result = service.update_movie(
            1,
            "Movie A",
            "Action",
            "English",
            120,
            "2026-11-30",
            "2026-10-01"
        )
        self.assertIsNone(result)
        mock_movie_dao.update_movie.assert_not_called()


