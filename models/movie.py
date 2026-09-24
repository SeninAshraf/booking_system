from dao.moviedao import MovieDao
from datetime import date
class movie:
    def __init__(self,movieId,movieTitle,movieGenre,movieLanguage,movieDuration,releaseDate,endDate):
        self.movieId=movieId
        self.movieTitle=movieTitle
        self.movieGenre=movieGenre
        self.movieLanguage=movieLanguage
        self.movieDuration=movieDuration
        self.releaseDate=releaseDate
        self.endDate=endDate
    def display(self):
        print("ID:",self.movieId)
        print("movie:",self.movieTitle)
        print("genre:",self.movieGenre)
        print("language:",self.movieLanguage)
        print("duration:",self.movieDuration)
        print("release date:",self.releaseDate)
        print("endDate",self.endDate)
movie1=movie(2,"BKU","comedy","malayalam","230 min",date(2026,9,4),date(2026,10,4))
movie1.display()
movie_dao=MovieDao()
movie_dao.add_movie(movie1)

