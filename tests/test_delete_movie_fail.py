# Test that delete_movie returns False when the DAO fails to delete the movie.
import unittest
from unittest.mock import Mock
from services.movieservice import MovieService
class TestMovieDeleteFailure(unittest.TestCase):
    def test_delete_movie_failure(self):
        mock_movie_dao = Mock()
        mock_movie_dao.delete_movie.return_value = False
        service = MovieService(mock_movie_dao)
        result = service.delete_movie(999)
        self.assertFalse(result)
        mock_movie_dao.delete_movie.assert_called_once_with(999)



    
