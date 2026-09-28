class Viewer:

    def starting_view(self, controller):

        print("""
================= MOVIE TICKET BOOKING SYSTEM =================

1. Admin
2. Theater Official
3. Customer
4. Exit

===============================================================
""")

        choice = input("SELECT YOUR ROLE: ")

        if choice == "1":
            self.login(controller)

        else:
            print("coming soon")

    def login(self, controller):

        username = input("Enter Username: ")
        password = input("Enter password: ")

        result = controller.login(username, password)

        if result:
            print("Login successful")
        else:
            print("Invalid username or password")