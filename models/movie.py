from dao.moviedao import MovieDao
from datetime import date
class Movie:
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



