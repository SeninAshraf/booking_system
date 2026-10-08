from datetime import datetime, date
class Viewer:

    def starting_view(self, controller,moviecontroller,theaterofficialcontroller,showcontroller):
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
                self.theater_login(controller,theaterofficialcontroller,showcontroller,moviecontroller)
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

    def theater_login(self,controller,theaterofficialcontroller,showcontroller,moviecontroller):
        print("==========THEATER OFFICIAL LOGIN==========")
        theater_name = input("Enter theater name:")
        theater_username = input("Enter theater user name:")
        theater_password = input("Enter theater password:")

        result = controller.theater_login(theater_name,theater_username,theater_password)
        if result:
            print("Login succesfull")
            theater_id = result.theater_id
            self.theaterofficial_menu(theaterofficialcontroller,showcontroller,moviecontroller,theater_id)
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

         return result

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

    def view_theater(self,theaterofficialcontroller):
             result = theaterofficialcontroller.view_theaters()
             
             if result:
                print("\n========== AVAILABLE THEATERS ==========\n")
                  
                print("Theater ID\tTheater Name")
                  
                for theater in result:
                    print(f"{theater[0]}\t\t{theater[1]}")
                print("These are the available Theaters..")
                return result
             else:
                  print("no theaters found...")

    def theaterofficial_menu(self,theaterofficialcontroller,showcontroller,moviecontroller,theater_id):
            while True:
                print("""
================= THEATER OFFICIAL MENU =================

1. Configure show
2. Update Show
3. Delete Show
4. View Show
5. Logout

=========================================================
                """)
                choice = input("SELECT AN OPTION: ")
                
                if choice == "1":
                        self.configure_show(moviecontroller,showcontroller,theater_id)
                elif choice == "2":
                        self.update_show(moviecontroller,showcontroller,theater_id)
                elif choice == "3":
                        print("coming soon")
                elif choice == "4":
                        self.view_show(showcontroller,theater_id)
                elif choice == "5":
                        print("exiting theater official menu...")
                        break
                else:
                    print("invalid option...")

    def configure_show(self, moviecontroller, showcontroller,theater_id):

        movies = self.view_movie(moviecontroller)

        try:
            choice = int(input("Enter Movie ID: "))
        except ValueError:
            print("Enter a valid Movie ID")
            return

        valid = False

        for movie in movies:
            if movie[0] == choice:
                valid = True
                break

        if not valid:
            print("Invalid Movie ID")
            return
        while True:
            try:
                screen_number = int(input("Enter Screen Number: "))
                break
            except ValueError:
                print("Enter valid  Number")
                
       

        while True:
            show_date = input("Enter Show Date (YYYY-MM-DD): ")

            try:
                    show_date = datetime.strptime(
                        show_date,
                        "%Y-%m-%d"
                    ).date()

                    if show_date < date.today():
                        print("Show date cannot be in the past.")
                        continue

                    break

            except ValueError:
                    print("Invalid date. Please use YYYY-MM-DD.")
        while True:
            start_time = input("Enter Start Time (HH:MM): ")

            try:
                start_time = datetime.strptime(
                    start_time,
                    "%H:%M"
                ).time()
                break

            except ValueError:
                print("Invalid start time. Please use HH:MM.")
        while True:
            end_time = input("Enter End Time (HH:MM): ")

            try:
                end_time = datetime.strptime(end_time,"%H:%M").time()

                if end_time <= start_time:
                    print("End time must be after start time.")
                    continue

                break

            except ValueError:
             print("Invalid end time. Please use HH:MM.")

        vip_rows, vip_seats, vip_price = self.get_seat_configuration("VIP")

        economy_rows, economy_seats, economy_price = self.get_seat_configuration("ECONOMY")

        result = showcontroller.add_show(
            choice,
            theater_id,
            screen_number,
            show_date,
            start_time,
            end_time,
        )
        if result is None:
            print("Show was NOT created.")
            return
        
        result_seat = showcontroller.add_seat(
             result,
             vip_rows,
             vip_seats,
             vip_price,
             economy_rows,
             economy_seats,
             economy_price
        )

        if result is not None and result_seat is not None:
            print("Show and seats created successfully")

    def get_seat_configuration(self, category):

        print(f"\n=== {category} SEATS ===")
        while True:
            try:
                rows = int(input("Enter Number of Rows: "))
                if rows <= 0:
                    print("Rows must be greater than 0.")
                    continue
                break
            except ValueError:
                 print("Enter a Valid Number")
        while True:
             try:
                seats_per_row = int(input("Enter Seats Per Row: "))
                if seats_per_row<=0:
                     print("Seats must be greater than 0")
                     continue
                break
             except ValueError:
                  print("Enter valid number")
        while True:
             try:
                price = float(input("Enter Ticket Price: "))
                if price <= 0:
                     print("Price must be greater than 0")
                     continue
                break
             except ValueError:
                  print("Enter a valid price")

        return rows, seats_per_row, price

    def update_show(self,moviecontroller,showcontroller,theater_id):
         self.view_show(showcontroller,moviecontroller,theater_id)
         while True:
            try:
                show_id =int(input("Enter id of show that needed to update:"))
            except ValueError:
                print("Enter invalid Id")
                continue
            result= self.search_show(showcontroller,show_id)
            if result:
                        show = result[0]
                        old_movie = show[1]
                        old_screen = show[2]
                        old_start = show[3]
                        old_end = show[4]
                        old_date = show[5]
                        print("Enter new values (Press Enter to keep the existing value)")  
                        movie = input(f"Movie [{old_movie}]: ")
                        if movie == "":
                            movie = old_movie
                        while True:
                            screen_numb = input(f"Enter Screen Number[{old_screen}]: ")
                            if screen_numb == "":
                                screen_number = old_screen
                                break
                            try:
                                screen_number = int(screen_numb)
                                break
                            except ValueError:
                                  print("Enter valid Number")
                            
                        while True:
                            show_date_input = input(
                                f"Enter Show Date (YYYY-MM-DD) [{old_date}]: "
                            )

                            if show_date_input == "":
                                show_date = old_date
                                break

                            try:
                                show_date = datetime.strptime(
                                    show_date_input,
                                    "%Y-%m-%d"
                                ).date()

                                if show_date < date.today():
                                    print("Show date cannot be in the past.")
                                    continue

                                break

                            except ValueError:
                                print("Invalid date. Please use YYYY-MM-DD.")
                            
                        while True:
                                    start_time_input = input(f"Enter Start Time (HH:MM)[{old_start}]: ")
                                    if start_time_input =="":
                                                    start_time=old_start
                                                    break
                        
                                    try:
                                        start_time = datetime.strptime(
                                            start_time_input,
                                            "%H:%M"
                                        ).time()
                                        break
                        
                                    except ValueError:
                                        print("Invalid start time. Please use HH:MM.")
                                    
                        while True:
                                    end_time_input = input(f"Enter End Time (HH:MM)[{old_end}]: ")
                                    if end_time_input =="":
                                                    end_time=old_end
                                                    break
                        
                                    try:
                                        end_time = datetime.strptime(end_time_input,"%H:%M").time()
                        
                                        if end_time <= start_time:
                                            print("End time must be after start time.")
                                            continue
                        
                                        break
                        
                                    except ValueError:
                                     print("Invalid end time. Please use HH:MM.")
                        
                        (old_vip_rows,
                                        old_vip_seats,
                                        old_vip_price,
                                        old_economy_rows,
                                        old_economy_seats,
                                        old_economy_price
                                    ) = self.get_old_seat_configuration(result)
                        vip_rows, vip_seats, vip_price = self.update_seat_configuration(
                                        "VIP",
                                        old_vip_rows,
                                        old_vip_seats,
                                        old_vip_price
                                    )
                        economy_rows, economy_seats, economy_price = self.update_seat_configuration(
                                    "ECONOMY",
                                    old_economy_rows,
                                    old_economy_seats,
                                    old_economy_price
                                )

                       
            else:
                          print("movie not found")
        
    def view_show(self,showcontroller,moviecontroller,theater_id):
         result = showcontroller.view_show(theater_id)
         if result:
                     print("\n========== AVAILABLE SHOWS ==========\n")
         
                     print("Show ID\t\tShow\t\tDate\t\tTime")
         
                     for show in result:
                         print(f"{show[0]}\t\t{show[1]}\t\t{show[2]}\t\t{show[3]}")
                     print("These are the available shows")
         else:
                       print("No movies available")
         
         return result

    def search_show(self, showcontroller, show_id):

        result = showcontroller.search_show(show_id)

        if result:

            print("\n========== SHOW DETAILS ==========\n")
            print(f"Movie Title       : {result[0][1]}")
            print(f"Screen Number     : {result[0][2]}")
            print(f"Start Time        : {result[0][3]}")
            print(f"End Time          : {result[0][4]}")
            print(f"Show Date         : {result[0][5]}")

            vip_rows = []
            vip_seat_count = 0
            vip_price = None

            for row in result:
                if row[6] == "VIP":

                    if row[7] not in vip_rows:
                        vip_rows.append(row[7])

                    vip_seat_count += 1
                    vip_price = row[8]

            print("\nFor VIP Category")
            print(f"Rows                    : {', '.join(vip_rows)}")
            print(f"No Of seats per row     : {vip_seat_count // len(vip_rows)}")
            print(f"Ticket Price             : {vip_price}")

            economy_rows = []
            economy_seat_count = 0
            economy_price = None

            for row in result:
                if row[6] == "Economy":

                    if row[7] not in economy_rows:
                        economy_rows.append(row[7])

                    economy_seat_count += 1
                    economy_price = row[8]

            print("\nFor Economy Category")
            print(f"Rows                    : {', '.join(economy_rows)}")
            print(f"No Of seats per row     : {economy_seat_count // len(economy_rows)}")
            print(f"Ticket Price             : {economy_price}")

            print("\n===================================")

            return result

    def get_old_seat_configuration(self, result):

        old_vip_rows = []
        old_vip_seat_count = 0
        old_vip_price = None

        old_economy_rows = []
        old_economy_seat_count = 0
        old_economy_price = None

        for row in result:

            if row[6] == "VIP":
                if row[7] not in old_vip_rows:
                    old_vip_rows.append(row[7])

                old_vip_seat_count += 1
                old_vip_price = row[8]

            elif row[6] == "Economy":
                if row[7] not in old_economy_rows:
                    old_economy_rows.append(row[7])

                old_economy_seat_count += 1
                old_economy_price = row[8]

        old_vip_seats = old_vip_seat_count // len(old_vip_rows)
        old_economy_seats = old_economy_seat_count // len(old_economy_rows)

        return (
            old_vip_rows,
            old_vip_seats,
            old_vip_price,
            old_economy_rows,
            old_economy_seats,
            old_economy_price
        )

    def update_seat_configuration(
        self,
        category,
        old_rows,
        old_seats_per_row,
        old_price
    ):

        print(f"\n=== UPDATE {category} SEATS ===")

    
        while True:
            rows_input = input(
                f"Enter Number of Rows [{old_rows}]: "
            )

            if rows_input == "":
                rows = old_rows
                break

            try:
                rows = int(rows_input)

                if rows <= 0:
                    print("Rows must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Enter a valid number.")

    
        while True:
            seats_input = input(
                f"Enter Seats Per Row [{old_seats_per_row}]: "
            )

            if seats_input == "":
                seats_per_row = old_seats_per_row
                break

            try:
                seats_per_row = int(seats_input)

                if seats_per_row <= 0:
                    print("Seats must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Enter a valid number.")

        
        while True:
            price_input = input(
                f"Enter Ticket Price [{old_price}]: "
            )

            if price_input == "":
                price = old_price
                break

            try:
                price = float(price_input)

                if price <= 0:
                    print("Price must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Enter a valid price.")

        return rows, seats_per_row, price