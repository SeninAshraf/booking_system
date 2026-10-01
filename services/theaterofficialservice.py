import bcrypt
from services.theaterservice import TheaterService
class TheaterofficialService:
    def __init__(self, theater_dao,theater_official_dao):
        self.theater_official_dao = theater_official_dao
        self.theater_dao = theater_dao

    def add_theater_user(self, theater_name, theater_username, password):
        result = self.theater_dao.get_theater(theater_name) 
        if not result:
            theater_id = self.theater_dao.add_theater(theater_name)
            if not theater_id:
                return False
        else:
            theater_id = result[0]
        existing_user = self.theater_official_dao.find_theater_user(theater_id)
        if existing_user:
            return False
        else:
            password_hash = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")
            return self.theater_official_dao.add_theateruser(
                theater_id,
                theater_username,
                password_hash
            )

    def check_user(self, theater_id):
        return self.theater_official_dao.find_theater_user(theater_id)




   
