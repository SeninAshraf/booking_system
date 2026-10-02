class ShowController:
    def __init__(self, showservice):
                self.showservice = showservice

    def add_show(self,choice,theater_id,screen_number,start_time,end_time,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
            return self.showservice.add_show(
                    choice,theater_id,screen_number,start_time,end_time,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy
            )