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

    def update_movie(self,movie_id,title1,genre1,language1,duration1,release_date1,end_date1):
        return self.movie_dao.update_movie(
            movie_id,title1,genre1,language1,duration1,release_date1,end_date1
        )