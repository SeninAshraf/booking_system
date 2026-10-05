class SeatService:
    def __init__(self, seat_dao):
        self.seat_dao = seat_dao

    def add_seats(self,show_id,vip_rows,vip_number_of_seats_per_row,ticket_price_vip,economy_rows,economy_number_of_seat_per_row,ticket_price_economy):
        for row in range(vip_rows):
            row_letter = chr(65 + row)

            for seat_number in range(1, vip_number_of_seats_per_row + 1):
                seat_no=f"{row_letter}{seat_number}"
                self.seat_dao.add_seat(
                    show_id,
                    seat_no,
                    "VIP",
                    "Available",
                    ticket_price_vip,
                    row_letter
                )

        for row in range(economy_rows):
                    row_letter = chr(65 + vip_rows + row)
        
                    for seat_number in range(1, economy_number_of_seat_per_row + 1):
                        seat_no=f"{row_letter}{seat_number}"
                        self.seat_dao.add_seat(
                            show_id,
                            seat_no,
                            "Economy",
                            "Available",
                            ticket_price_economy,
                            row_letter
                        )
