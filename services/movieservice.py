class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def add_movie(self,title,genre,language,duration,release_date,end_date):
        if end_date<release_date:#check date end date is lesser than release date
            return None#result failed
        else:
            return self.movie_dao.add_movie(#else add movie details
                title,genre,language,duration,release_date,end_date
            )

    def view_movie(self):
        return self.movie_dao.view_movie()#pass to movie_dao and return to contr

    def search_movie(self,movie_id):
        return self.movie_dao.get_movie(movie_id)

    def delete_movie(self,movie_id):
        return self.movie_dao.delete_movie(movie_id)#call dao and perform delete movie sql query

    def update_movie(self,movie_id,title1,genre1,language1,duration1,release_date1,end_date1):
        if end_date1<release_date1:#check date validation and if yes return fail
            return None
        else:
            return self.movie_dao.update_movie(#else add to sql with new value
                movie_id,title1,genre1,language1,duration1,release_date1,end_date1
            )