from datetime import date
class show:
    def __init__(self,showId,screenNo,startTime,endTime,showDate):
        self.showId=showId
        self.screenNo=screenNo
        self.startTime=startTime
        self.endTime=endTime
        self.showDate=showDate
    def display(self):
        print("show id:",self.showId)
        print("screen No:",self.screenNo)
        print("start Time:",self.startTime)
        print("end Time:",self.endTime)
        print("show Date:",self.showDate)
show1=show(1,1,"9:30","12:30",date(2026,9,6))
show1.display()