from dao.theaterdao import TheaterDao
class Theater:
    def __init__(self,theater_id,theaterName):
        self.theater_id=theater_id
        self.theaterName=theaterName
    def display(self):
        print("Theater Id:",self.theater_id)
        print("Theater Name:",self.theaterName)


