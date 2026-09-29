class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def add_movie(self,title,genre,language,duration,release_date,end_date):
        print("service")