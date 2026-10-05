class ShowService:
    def __init__(self, show_dao):
        self.show_dao = show_dao

    def add_show(self,choice,theater_id,screen_number,show_date,start_time,end_time,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
        return self.show_dao.add_show(
                            choice,theater_id,screen_number,show_date,start_time,end_time,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy
                    )