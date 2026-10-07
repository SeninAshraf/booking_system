from datetime import datetime , date
class ShowService:
    def __init__(self, show_dao,movie_dao):
        self.show_dao = show_dao
        self.movie_dao = movie_dao

    def add_show(self,choice,theater_id,screen_number,show_date,start_time,end_time):
        movie = self.movie_dao.get_movie(choice)
        release_date = movie[5]
        end_date = movie[6]
        release_date = datetime.strptime( release_date,
                    "%Y-%m-%d"
                ).date()
        
        end_date = datetime.strptime( end_date,
                    "%Y-%m-%d"
                ).date()
        if show_date<release_date:
            print("this show date is before the release date ")
            return None
        elif show_date>end_date:
             print("this show date is after the release date ")
             return None
        else:
            collision = self.show_dao.check_show_collision(theater_id,screen_number,show_date.strftime("%Y-%m-%d"),
    start_time.strftime("%H:%M"),
    end_time.strftime("%H:%M"))

            if collision:
                print("Show collision! This screen is already occupied.")
                return None
            else:
                return self.show_dao.add_show(
                                choice,theater_id,screen_number, start_time.strftime("%H:%M"),
    end_time.strftime("%H:%M"),
    show_date.strftime("%Y-%m-%d")
                        )

    def view_show(self,theater_id):
            return self.show_dao.get_all(theater_id)

    def search_show(self,show_id):
            return self.show_dao.search_show(show_id)
    