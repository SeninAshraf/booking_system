class Viewer:

    def starting_view(self, controller,moviecontroller):

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
            self.login(controller,moviecontroller)
        elif choice == "2":
            self.theater_login(controller)
        elif choice == "3":
            self.customer_login(controller)
        elif choice == "4":
            self.exit()
        else:
            print("coming soon")

    def login(self, controller,moviecontroller):

        username = input("Enter Username: ")
        password = input("Enter password: ")

        result = controller.login(username, password)

        if result:
            print("Login successful")
            self.admin_menu(moviecontroller)
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
        while True:
            print("========== CUSTOMER ==========")
            try:
                customer_mobile_num = int(input("Enter mobile number:"))
                break
            except ValueError:
                print("please enter valid number")

    def exit(self):
        print("Thank you for using Movie Ticket Booking System.")
        return

    def admin_menu(self,moviecontroller):
        print("""
================= ADMIN MENU =================
        
    1. Create Theater Official
    2. View Movies
    3. Add Movie
    4. Update Movie
    5. Delete Movie
    6. View Transactions
    7. Logout
        
==============================================
        """)
        choice = input("SELECT YOUR ROLE: ")
        
        if choice == "1":
                print("coming soon")
        elif choice == "2":
                self.view_movie(moviecontroller)
        elif choice == "3":
                self.add_movie(moviecontroller)
        elif choice == "3":
                print("coming soon")
        elif choice == "4":
                self.exit()
        else:
            print("coming soon")

    def add_movie(self,moviecontroller):
        title = input("Enter Movie Title: ")
        genre = input("Enter Genre: ")
        language = input("Enter Language: ")
        duration = input("Enter Duration (minutes): ")
        release_date = input("Enter Release Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")

        result = moviecontroller.add_movie(title,genre,language,duration,release_date,end_date)
        if result:
                print("Added Succesfull")
        else:
                print("Adding Failed")

    def view_movie(self,moviecontroller):
         result = moviecontroller.view_movie()
         if result:
            print("\n========== AVAILABLE MOVIE ==========\n")

            print("Movie ID\tMovie")

            for movie in result:
                print(f"{movie[0]}\t\t{movie[1]}")
            print("These are the available movies")
         else:
              print("No movies available")
              