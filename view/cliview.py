class Viewer:

    def starting_view(self, controller,moviecontroller,theaterofficialcontroller):
        while True:
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
                self.login(controller,moviecontroller,theaterofficialcontroller)
            elif choice == "2":
                self.theater_login(controller)
            elif choice == "3":
                self.customer_login(controller)
            elif choice == "4":
                self.exit()
                break
            else:
                print("choose only appropriate role's option")

    def login(self, controller,moviecontroller,theaterofficialcontroller):

        username = input("Enter Username: ")
        password = input("Enter password: ")

        result = controller.login(username, password)

        if result:
            print("Login successful")
            self.admin_menu(moviecontroller,theaterofficialcontroller)
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

    def admin_menu(self,moviecontroller,theaterofficialcontroller):
        while True:
            print("""
================= ADMIN MENU =================
            
    1. Create Theater Official
    2. View Movies
    3. Add Movie
    4. Update Movie
    5. Delete Movie
    6. View Transactions
    7. Exit Admin menu
            
==============================================
            """)
            choice = input("SELECT AN OPTION: ")
            
            if choice == "1":
                    self.add_theater_user(theaterofficialcontroller)
            elif choice == "2":
                    self.view_movie(moviecontroller)
            elif choice == "3":
                    self.add_movie(moviecontroller)
            elif choice == "4":
                    self.update_movie(moviecontroller)
            elif choice == "5":
                    self.delete_movie(moviecontroller)
            elif choice == "6":
                    print("coming soon")
            elif choice == "7":
                print("Logging out...")
                break
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
                print("Adding Failed or missmatch of dates are found!!!")

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

    def update_movie(self,moviecontroller):
         self.view_movie(moviecontroller)
         movie_id = int(input("Enter movie_id "))
         result= self.search_movie(moviecontroller,movie_id)
         if result:
            print("Enter new values (Press Enter to keep the existing value)")  
            title1 = input("Enter Movie Title: ")
            genre1 = input("Enter Genre: ")
            language1 = input("Enter Language: ")
            duration1 = input("Enter Duration (minutes): ")
            release_date1 = input("Enter Release Date (YYYY-MM-DD): ")
            end_date1 = input("Enter End Date (YYYY-MM-DD): ")
            title1 = title1 if title1 else result[1]
            genre1 = genre1 if genre1 else result[2]
            language1 = language1 if language1 else result[3]
            duration1 = duration1 if duration1 else result[4]
            release_date1 = release_date1 if release_date1 else result[5]
            end_date1 = end_date1 if end_date1 else result[6]
            result1 = moviecontroller.update_movie(movie_id,title1,genre1,language1,duration1,release_date1,end_date1)
            if result1:
                print("updating Movie..\nMovie Updated Succesfully\nReturning To Admin Menu....")
            else:
                print("updation failed or missmatch of date found!!!")
         else:
              print("movie not found")

    def delete_movie(self,moviecontroller):
         self.view_movie(moviecontroller)
         movie_id = int(input("Enter movie_id "))
         self.search_movie(moviecontroller,movie_id)
         print("\nDo you want to delete this movie?")
         print("1. Yes")
         print("2. No")
         choice = int(input("Select an Option: "))
         if choice == 1:
              result = moviecontroller.delete_movie(movie_id)
              if result:
                   print("movie deleted succesfully")
              else:
                   print("deletion failed")
         elif choice == 2:
              print("deletion cancelled")
         else:
              print("Invalid option.")

    def search_movie(self,moviecontroller,movie_id):
         result = moviecontroller.search_movie(movie_id)
         
         if result:
              print("\n========== MOVIE DETAILS ==========\n")
              print(f"Movie Title  : {result[1]}")
              print(f"Genre        : {result[2]}")
              print(f"Language     : {result[3]}")
              print(f"Duration     : {result[4]}")
              print(f"Release Date : {result[5]}")
              print(f"End Date     : {result[6]}")
              print("\n===================================")

              return result
         else:
              print("no movie found...")

    def add_theater_user(self,theaterofficialcontroller):
         theater_name = input("Enter theater Name:")
         theater_username = input("Enter Username")
         password = input("Enter Password:")

         result = theaterofficialcontroller.add_theater_user(theater_name,theater_username,password)

         if result:
              print("Theater user added succesfully.")
         else:
              print("user addition failed.")