class Viewer:

    def login(self, controllers):

        username = input("Enter Username: ")
        password = input("Enter password: ")

        result = controllers.login(username, password)

        if result:
            print("Login successful")
        else:
            print("Invalid username or password")