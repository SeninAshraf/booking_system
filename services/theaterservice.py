class TheaterService:
    def __init__(self, theater_dao):
            self.theater_dao = theater_dao

    #def check_theater(self,theater_name):
            #return self.theater_dao.get_theater(theater_name)

    def view_theaters(self):
          return self.theater_dao.view_theaters()

    def view_movie_based_theater(self,choice):
          result= self.theater_dao.view_movie_based_theater(choice)
          if result:
                print("====AVAILABLE THEATERS====")
                print("Theater ID\tTheater Name")
                for theater in result:
                        print(f"{theater[0]}\t\t{theater[1]}")
                        print("These are the available Theaters..")
                        return result
          else:
                        print("no theaters found...")
