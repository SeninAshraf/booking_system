class MovieController:
    def __init__(self, movieservice):
            self.movieservice = movieservice

    def add_movie(self,title,genre,language,duration,release_date,end_date):
          return self.movieservice.add_movie(#pass to movieservice.add_movie method with 5 input
                title,genre,
                language,
                duration,
                release_date,
                end_date
          )

    def view_movie(self):#pass to movieservice method= view movie 
          return self.movieservice.view_movie()#return the result to view class

    def search_movie(self,movie_id):
          return self.movieservice.search_movie(movie_id)

    def delete_movie(self,movie_id):#pass to movie service and call delete movie method
          return self.movieservice.delete_movie(movie_id)

    def update_movie(self,movie_id,title1,genre1,language1,duration1,release_date1,end_date1):#pass the value to update movie in service class
          return self.movieservice.update_movie(
                movie_id,title1,genre1,language1,duration1,release_date1,end_date1
          )