# Test that update_movie updates the movie when the dates are valid.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieUpdate(unittest.TestCase):
    def test_update_movie_success(self):
        mock_movie_dao = Mock()
        mock_movie_dao.update_movie.return_value = True

        service = MovieService(mock_movie_dao)

        result = service.update_movie(
            1,
            "Aryan",
            "Thriller",
            "Tamil",
            140,
            "2026-10-15",
            "2026-11-30"
        )
        self.assertTrue(result)
        mock_movie_dao.update_movie.assert_called_once_with(
            1,
            "Aryan",
            "Thriller",
            "Tamil",
            140,
            "2026-10-15",
            "2026-11-30"
        )


