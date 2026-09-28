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
        elif choice == "2":
            self.theater_login(controller)
        elif choice == "3":
            self.customer_login(controller)
        elif choice == "4":
            self.exit()
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

    def theater_login(self,controller):
        print("==========THEATER OFFICIAL LOGIN==========")
        theater_name = input("Enter theater name:")
        theater_username = input("Enter theater user name:")
        theater_password = input("Enter theater password:")

        result = controller.theater_login(theater_name,theater_username,theater_password)
        if result:
            print("Login succesfull")
        else:
            print("Invalid username or theatername or password")

    def customer_login(self,controller):
        print("========== CUSTOMER ==========")
        customer_mobile_num = input("Enter mobile number:")

    def exit(self):
        print("Thank you for using Movie Ticket Booking System.")
        return