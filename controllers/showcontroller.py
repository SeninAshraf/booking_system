class ShowController:
    def __init__(self, showservice,seatservice):
                self.showservice = showservice
                self.seatservice = seatservice

    def add_show(self,choice,theater_id,screen_number,show_date,start_time,end_time):
            return self.showservice.add_show(
                    choice,theater_id,screen_number,show_date,start_time,end_time)

    def add_seat(self,result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
                return self.seatservice.add_seats(
                        result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy
                )

    def view_show(self,theater_id):
                return self.showservice.view_show(theater_id)

    def search_show(self,show_id):
              return self.showservice.search_show(show_id)

    def update_show(self,show_id,screen_number,show_date,start_time,end_time):
            return self.showservice.update_show(show_id,screen_number,show_date,start_time,end_time)

    def update_seats(self,show_id,vip_rows,
                                     vip_seats,
                                     vip_price,
                                     economy_rows,
                                     economy_seats,
                                     economy_price):
            return self.seatservice.update_seats(show_id,vip_rows,
                                     vip_seats,
                                     vip_price,
                                     economy_rows,
                                     economy_seats,
                                     economy_price)

    def delete_show(self, show_id):

        result_show = self.showservice.delete_show(show_id)
        result_seat = self.seatservice.delete_seat(show_id)

        if result_show and result_seat:
                return True

        return False