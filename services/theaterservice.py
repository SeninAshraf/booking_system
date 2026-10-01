class TheaterService:
    def __init__(self, theater_dao):
            self.theater_dao = theater_dao

    #def check_theater(self,theater_name):
            #return self.theater_dao.get_theater(theater_name)

    def view_theaters(self):
          return self.theater_dao.view_theaters()