from dao.showdao import ShowDao
from datetime import date
class Show:
    def __init__(self,showId,movieId,theater_id,screenNo,startTime,endTime,showDate):
        self.showId=showId
        self.movieId=movieId
        self.theater_id=theater_id
        self.screenNo=screenNo
        self.startTime=startTime
        self.endTime=endTime
        self.showDate=showDate
    def display(self):
        print("showId:",self.showId)
        print("movie id:",self.movieId)
        print("theater id:",self.theater_id)
        print("screen No:",self.screenNo)
        print("start Time:",self.startTime)
        print("end Time:",self.endTime)
        print("show Date:",self.showDate)

