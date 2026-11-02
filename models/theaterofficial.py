class TheaterOfficial:

    def __init__(self, theater_id,theaterUserName, passwordHash, firstLogin):
        self.theater_id=theater_id
        self.theaterUserName = theaterUserName
        self.passwordHash = passwordHash
        self.firstLogin = firstLogin
    def display(self):
        print("Theater ID:",self.theater_id)
        print("Theater Username:",self.theaterUserName)
        print("Password:",self.passwordHash)
        print("Is first login:",self.firstLogin)
