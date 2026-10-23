# Test that delete_movie returns True when the DAO successfully deletes the movie.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieDelete(unittest.TestCase):
    def test_delete_movie_success(self):
        mock_movie_dao = Mock()
        mock_movie_dao.delete_movie.return_value = True
        service = MovieService(mock_movie_dao)
        result = service.delete_movie(1)
        self.assertTrue(result)
        mock_movie_dao.delete_movie.assert_called_once_with(1)