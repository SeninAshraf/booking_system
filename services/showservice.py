class ShowService:
    def __init__(self, show_dao):
        self.show_dao = show_dao

    def add_show(self,choice,theater_id,screen_number,show_date,start_time,end_time):
        return self.show_dao.add_show(
                            choice,theater_id,screen_number,show_date,start_time,end_time
                    )