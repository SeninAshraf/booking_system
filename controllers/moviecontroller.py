class MovieController:
    def __init__(self, movieservice):
            self.movieservice = movieservice

    def add_movie(self,title,genre,language,duration,release_date,end_date):
          return self.movieservice.add_movie(
                title,genre,
                language,
                duration,
                release_date,
                end_date
          )

    def view_movie(self):
          return self.movieservice.view_movie()

    def search_movie(self,movie_id):
          return self.movieservice.search_movie(movie_id)

    def delete_movie(self,movie_id):
          return self.movieservice.delete_movie(movie_id)