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