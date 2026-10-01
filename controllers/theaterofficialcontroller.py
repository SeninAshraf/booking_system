class TheaterofficialController:
    def __init__(self, theater_official_service,theater_service):
        self.theater_official_service = theater_official_service
        self.theater_service = theater_service

    def add_theater_user(self,theater_name,theater_username,password):
        return self.theater_official_service.add_theater_user(theater_name,theater_username,password)

    def view_theaters(self):
        return self.theater_service.view_theaters()