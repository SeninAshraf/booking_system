from dao.theaterdao import TheaterDao
class theater:
    def __init__(self,theater_id,theaterName):
        self.theater_id=theater_id
        self.theaterName=theaterName
    def display(self):
        print("Theater Id:",self.theater_id)
        print("Theater Name:",self.theaterName)
theater1=theater(1,"Muri")
#theater1.display()

theater_dao = TheaterDao()
#theater_dao.add_theater(theater1)
#theater_dao.update_theater(theater1)
print(theater_dao.get_theater("muri"))
