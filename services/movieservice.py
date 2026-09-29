class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def add_movie(self,title,genre,language,duration,release_date,end_date):
        return self.movie_dao.add_movie(
            title,genre,language,duration,release_date,end_date
        )

    def view_movie(self):
        return self.movie_dao.view_movie()

    def search_movie(self,movie_id):
        return self.movie_dao.get_movie(movie_id)

    def delete_movie(self,movie_id):
        return self.movie_dao.delete_movie(movie_id)