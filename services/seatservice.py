class SeatService:
    def __init__(self, seat_dao):
        self.seat_dao = seat_dao

    def add_seats(self,result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
        return self.show_dao.add_show(
                            result,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy
                    )