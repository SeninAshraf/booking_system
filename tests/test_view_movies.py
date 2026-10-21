# Test that view_movie returns the movie list provided by the DAO.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieView(unittest.TestCase):
    def test_view_movie(self):
        mock_movie_dao = Mock()
        expected_movies = [
            (1, "Movie A", "Action", "English", 120, "2026-10-01", "2026-11-30"),
            (2, "Movie B", "Comedy", "Malayalam", 150, "2026-10-05", "2026-12-01")
        ]
        mock_movie_dao.view_movie.return_value = expected_movies
        service = MovieService(mock_movie_dao)
        result = service.view_movie()
        self.assertEqual(result, expected_movies)
        mock_movie_dao.view_movie.assert_called_once_with()


