# Test that search_movie returns None when the movie ID does not exist.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieSearchNotFound(unittest.TestCase):
  def test_search_movie_not_found(self):
        mock_movie_dao = Mock()
        mock_movie_dao.get_movie.return_value = None
        service = MovieService(mock_movie_dao)
        result = service.search_movie(999)
        self.assertIsNone(result)
        mock_movie_dao.get_movie.assert_called_once_with(999)


