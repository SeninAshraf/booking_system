class ShowController:
    def __init__(self, showservice,seatservice):
                self.showservice = showservice
                self.seatservice = seatservice

    def add_show(self,choice,theater_id,screen_number,show_date,start_time,end_time):
            return self.showservice.add_show(
                    choice,theater_id,screen_number,show_date,start_time,end_time)

    def add_seat(self,result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
                return self.seatservice.add_show(
                        result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy
                )