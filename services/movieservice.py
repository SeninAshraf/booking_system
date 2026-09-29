class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def add_movie(self,title,genre,language,duration,release_date,end_date):
        return self.movie_dao.add_movie(
            title,genre,language,duration,release_date,end_date
        )

    def view_movie(self):
        return self.movie_dao.view_movie()