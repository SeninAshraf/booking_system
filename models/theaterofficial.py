class TheaterOfficial:

    def __init__(self, theaterUserName, passwordHash, firstLogin):
        self.theaterUserName = theaterUserName
        self.passwordHash = passwordHash
        self.firstLogin = firstLogin
    def display(self):
        print("Theater Username:",self.theaterUserName)
        print("Password:",self.passwordHash)
        print("Is first login:",self.firstLogin)
TheaterOfficial1=TheaterOfficial("senin","****","yes")
TheaterOfficial1.display()
