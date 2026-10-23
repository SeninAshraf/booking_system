# Test that search_movie returns the movie details for the given movie ID.

import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieSearch(unittest.TestCase):
    def test_search_movie(self):
        mock_movie_dao = Mock()
        expected_movie = (
            1, "Chindamani Kolacase", "Action", "Malayalam", 120,
            "2026-10-01", "2026-11-30"
        )
        mock_movie_dao.get_movie.return_value = expected_movie
        service = MovieService(mock_movie_dao)
        result = service.search_movie(1)
        self.assertEqual(result, expected_movie)
        mock_movie_dao.get_movie.assert_called_once_with(1)

