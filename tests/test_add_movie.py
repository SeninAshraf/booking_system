#This test assumes your DAO accepts date strings in YYYY-MM-DD format and returns True when the movie is successfully added.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieAdd(unittest.TestCase):

    def test_add_movie_success(self):
        mock_movie_dao = Mock()
        mock_movie_dao.add_movie.return_value = True
        service = MovieService(mock_movie_dao)
        result = service.add_movie(
            "Movie A",
            "Action",
            "English",
            120,
            "2026-10-01",
            "2026-11-30"
        )
        self.assertTrue(result)
        mock_movie_dao.add_movie.assert_called_once_with(
            "Movie A",
            "Action",
            "English",
            120,
            "2026-10-01",
            "2026-11-30"
        )



