import bcrypt
from services.theaterservice import TheaterService
class TheaterofficialService:
    def __init__(self, theater_dao,theater_official_dao):
        self.theater_official_dao = theater_official_dao
        self.theater_dao = theater_dao

    def add_theater_user(self, theater_name, theater_username, password):
        result = self.theater_dao.get_theater(theater_name) #check if the theater with same name  exist in dao
        if not result:
            theater_id = self.theater_dao.add_theater(theater_name)#add the theater and retrieve id
            if not theater_id:
                return False#retrun none
        else:
            theater_id = result[0]#sql first index will be id
        existing_user = self.theater_official_dao.find_theater_user(theater_id)#find theater user in dao
        if existing_user:
            return False
        else:
            password_hash = bcrypt.hashpw(#else convert newly created pass to pass_hash with bcrypt
                password.encode("utf-8"),
                bcrypt.gensalt()#generate random salt like random numb
            ).decode("utf-8")#standard way for understand computer and represent test as bytes 
            return self.theater_official_dao.add_theateruser(#add theater user with 3 input pass to dao
                theater_id,
                theater_username,
                password_hash
            )

    def check_user(self, theater_id):
        return self.theater_official_dao.find_theater_user(theater_id)




   
