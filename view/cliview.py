from datetime import datetime, date#for today date
class Viewer:
#FIRST CALL THIS FUNCTION THEN PRINT MENU
    def starting_view(self, controller,moviecontroller,theaterofficialcontroller,showcontroller,bookingcontroller,reportingcontroller):
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
                self.login(controller,moviecontroller,theaterofficialcontroller,bookingcontroller,reportingcontroller)
            elif choice == "2":
                self.theater_login(controller,theaterofficialcontroller,showcontroller,moviecontroller)#call theater login method in this class or object(self)
            elif choice == "3":
                self.customer_login(controller,moviecontroller,theaterofficialcontroller,showcontroller,bookingcontroller)
            elif choice == "4":
                self.exit()
                break
            else:
                print("choose only appropriate role's option")

    def login(self, controller,moviecontroller,theaterofficialcontroller,bookingcontroller,reportingcontroller):

        username = input("Enter Username: ")
        password = input("Enter password: ")

        result = controller.login(username, password)#MOVE TO CONTROLLER LOGIN METHOD

        if result:#IF RESULT THEN PRINT AND MOVE TO ADMIN MENU
            print("Login successful")
            self.admin_menu(moviecontroller,theaterofficialcontroller,reportingcontroller)#CURRENT OBJECT METHOD
        else:
            print("Invalid username or password")

    def theater_login(self,controller,theaterofficialcontroller,showcontroller,moviecontroller):
        print("==========THEATER OFFICIAL LOGIN==========")
        theater_name = input("Enter theater name:")
        theater_username = input("Enter theater user name:")
        theater_password = input("Enter theater password:")

        result = controller.theater_login(theater_name,theater_username,theater_password)#pass to controller
        if result:
            print("Login succesfull")
            theater_id = result.theater_id#here it get the theater id 
            self.theaterofficial_menu(theaterofficialcontroller,showcontroller,moviecontroller,theater_id)#pass to theater official menu with this parameters
        else:
            print("Invalid username or theatername or password")

    
    
    def customer_login(self, controller, moviecontroller,
                    theaterofficialcontroller, showcontroller,bookingcontroller):

        while True:
            print("========== CUSTOMER ==========")
            customer_mobile_num = input("Enter mobile number: ").strip()#removes whitespace from the beginning and end of a string.

            if not customer_mobile_num.isdigit():#checks whether a string contains only digits 
                print("Please enter a valid mobile number.")
                continue

            break

        result = controller.customer_login(customer_mobile_num)#pas sto customer login in controller(auth)

        if result:
            customer_id = result[0]#if existing user retrive id
            print(f"Customer ID is {customer_id}")

        else:
            print("New customer detected. Registering...")
            new_user = controller.new_customer_login(customer_mobile_num)#if new . then pass to controller auth

            if new_user:
                print("Customer added successfully.")
                result = controller.customer_login(customer_mobile_num)
                if result:
                    customer_id = result[0]
                    print(f"Customer ID is {customer_id}")
                else:
                    print("Unable to retrieve customer details.")
                    return
            else:
                print("Customer addition failed.")
                return
        self.customer_menu(#then call customer_menu with  4 parameters values
            customer_id,
            moviecontroller,
            theaterofficialcontroller,
            showcontroller,bookingcontroller
        )

    def exit(self):
        print("Thank you for using Movie Ticket Booking System.")
        return

    def admin_menu(self,moviecontroller,theaterofficialcontroller,bookingcontroller):
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
                    self.view_movie(moviecontroller)#use ith thru moviecontroller
            elif choice == "3":
                    self.add_movie(moviecontroller)
            elif choice == "4":
                    self.update_movie(moviecontroller)
            elif choice == "5":
                    self.delete_movie(moviecontroller)
            elif choice == "6":
                    self.view_transaction(bookingcontroller)
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
        if not title or not genre or not language or not duration or not release_date or not end_date:
                    print("All fields are required.")
                    return

        result = moviecontroller.add_movie(title,genre,language,duration,release_date,end_date)#pass to moviecontroller
        if result:
                print("Added Succesfull")
        else:
                print("Adding Failed or missmatch of dates are found!!!")

    def view_movie(self,moviecontroller):
         result = moviecontroller.view_movie()#caall view_movie method in moviecontroller
         if result:
            print("\n========== AVAILABLE MOVIE ==========\n")

            print("Movie ID\tMovie")

            for movie in result:
                print(f"{movie[0]}\t\t{movie[1]}")#print id name 
            print("These are the available movies")
         else:
              print("No movies available")

         return result

    def update_movie(self,moviecontroller):
         self.view_movie(moviecontroller)#view all movies
         movie_id = int(input("Enter movie_id "))#enter the movie id
         result= self.search_movie(moviecontroller,movie_id)#call the searchmovie function
         if result:
            print("Enter new values (Press Enter to keep the existing value)")  
            title1 = input("Enter Movie Title: ")
            genre1 = input("Enter Genre: ")
            language1 = input("Enter Language: ")
            while True:
                duration1 = input("Enter Duration (minutes): ")

                if duration1 == "":
                    break

                try:
                    duration1 = int(duration1)
                    if duration1 <= 0:
                        print("Duration must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Enter duration in numbers only.")
            release_date1 = input("Enter Release Date (YYYY-MM-DD): ")
            end_date1 = input("Enter End Date (YYYY-MM-DD): ")
            title1 = title1 if title1 else result[1]#add input as new value if user eneter anyinput other wise old value its called terinary operator
            genre1 = genre1 if genre1 else result[2]
            language1 = language1 if language1 else result[3]
            duration1 = duration1 if duration1 else result[4]
            release_date1 = release_date1 if release_date1 else result[5]
            end_date1 = end_date1 if end_date1 else result[6]
            result1 = moviecontroller.update_movie(movie_id,title1,genre1,language1,duration1,release_date1,end_date1)#pass the value to movie controller
            if result1:
                print("updating Movie..\nMovie Updated Succesfully\nReturning To Admin Menu....")
            else:
                print("updation failed or missmatch of date found!!!")
         else:
              print("movie not found")

    def delete_movie(self,moviecontroller):
         self.view_movie(moviecontroller)#view movie
         movie_id = int(input("Enter movie_id "))#id
         result=self.search_movie(moviecontroller,movie_id)#serach movie with id
         if not result:
              print("No movie found")
              return
         print("\nDo you want to delete this movie?")
         print("1. Yes")
         print("2. No")
         choice = int(input("Select an Option: "))
         if choice == 1:
              result = moviecontroller.delete_movie(movie_id)#pass to movie controller and  call delete movie method
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
         password = input("Enter Password:")#receive inputs from uswr
         if not theater_name or not theater_username or not password:
            print("All fields are required.")
            return
         result = theaterofficialcontroller.add_theater_user(theater_name,theater_username,password)#pass to theater official controll

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
                        self.configure_show(moviecontroller,showcontroller,theater_id)#pass to this class object method
                elif choice == "2":
                        self.update_show(moviecontroller,showcontroller,theater_id)
                elif choice == "3":
                        self.delete_show(moviecontroller,showcontroller,theater_id)
                elif choice == "4":
                        self.view_show(showcontroller,moviecontroller,theater_id)
                elif choice == "5":
                        print("exiting theater official menu...")
                        break
                else:
                    print("invalid option...")

    def configure_show(self, moviecontroller, showcontroller,theater_id):

        movies = self.view_movie(moviecontroller)#call view_movie method

        try:
            choice = int(input("Enter Movie ID: "))#id
        except ValueError:
            print("Enter a valid Movie ID")
            return

        valid = False

        for movie in movies:
            if movie[0] == choice:#the user input only receive when the corresponding number must be in list of view movies
                valid = True
                break

        if not valid:
            print("Invalid Movie ID")
            return
        while True:
            try:
                screen_number = int(input("Enter Screen Number: "))#screeen num
                break
            except ValueError:
                print("Enter valid  Number")
                
       

        while True:
            show_date = input("Enter Show Date (YYYY-MM-DD): ")#show date in format

            try:
                    show_date = datetime.strptime(#convert into satndard format of date
                        show_date,
                        "%Y-%m-%d"
                    ).date()

                    if show_date < date.today():#if user tries to enter yesterday's or past date
                        print("Show date cannot be in the past.")
                        continue

                    break

            except ValueError:#if not in format raise error
                    print("Invalid date. Please use YYYY-MM-DD.")
        while True:
            start_time = input("Enter Start Time (HH:MM): ")#enter time in format

            try:
                start_time = datetime.strptime(#convert time in standard format
                    start_time,
                    "%H:%M"
                ).time()
                break

            except ValueError:
                print("Invalid start time. Please use HH:MM.")#raise error if it didnt follow format
        while True:
            end_time = input("Enter End Time (HH:MM): ")#same as of start_time

            try:
                end_time = datetime.strptime(end_time,"%H:%M").time()

                if end_time <= start_time:#validate time in start time > end time 
                    print("End time must be after start time.")
                    continue

                break

            except ValueError:
             print("Invalid end time. Please use HH:MM.")

        vip_rows, vip_seats, vip_price = self.get_seat_configuration("VIP")#call get_seat_configuration to enetr vip, seats or eceonomy

        economy_rows, economy_seats, economy_price = self.get_seat_configuration("ECONOMY")

        result = showcontroller.add_show(#pass this to  show controller with this parametrs
            choice,
            theater_id,
            screen_number,
            show_date,
            start_time,
            end_time,
        )
        if result is None:#if result failed then it raise message no creation
            print("Show was NOT created.")
            return
        
        result_seat = showcontroller.add_seat(#if it gives show id then it. call add seat in show controller
             result,
             vip_rows,
             vip_seats,
             vip_price,
             economy_rows,
             economy_seats,
             economy_price
        )

        if result is not None and result_seat is not None:#if any of fail didnt work other wise print succesfull msg
            print("Show and seats created successfully")

    def get_seat_configuration(self, category):

        print(f"\n=== {category} SEATS ===")#vip seats
        while True:
            try:
                rows = int(input("Enter Number of Rows: "))
                if rows <= 0:#row is -0 then fail
                    print("Rows must be greater than 0.")
                    continue
                break
            except ValueError:
                 print("Enter a Valid Number")
        while True:
             try:
                seats_per_row = int(input("Enter Seats Per Row: "))#seat per row 
                if seats_per_row<=0:#if row is -9
                     print("Seats must be greater than 0")
                     continue
                break
             except ValueError:
                  print("Enter valid number")
        while True:
             try:
                price = float(input("Enter Ticket Price: "))
                if price <= 0:#if price is -900
                     print("Price must be greater than 0")
                     continue
                break
             except ValueError:
                  print("Enter a valid price")

        return rows, seats_per_row, price#retrun that with 3 parameters

    def update_show(self,moviecontroller,showcontroller,theater_id):
         result=self.view_show(showcontroller,moviecontroller,theater_id)#view all shows based on theater id
         if not  result:
              return#confusing
         while True:
            try:
                show_id =int(input("Enter id of show that needed to update:"))#id for update show
            except ValueError:
                print("Enter invalid Id")
                continue
            result= self.search_show(showcontroller,show_id)#show searching
            
            if result:
                        show = result[0]
                        old_movie = show[1]
                        old_screen = show[2]
                        old_start = show[3]
                        old_end = show[4]
                        old_date = show[5]
                        print(f"Enter Updated Values for the show of{old_movie} ")
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
                                    print("Show date cannot be in the past.")#validation
                                    continue

                                break

                            except ValueError:
                                print("Invalid date. Please use YYYY-MM-DD.")#raise error
                            
                        while True:
                                    start_time_input = input(f"Enter Start Time (HH:MM)[{old_start}]: ")
                                    if start_time_input =="":
                                                    start_time=old_start
                                                    break
                        
                                    try:
                                        start_time = datetime.strptime(#convertion into time format
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
                        
                                        if end_time <= start_time:#validation if end_time<start_time
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
                                    ) = self.get_old_seat_configuration(result)#for getting exact amount of like number of rows =3 number of seat per row = 10
                        vip_rows, vip_seats, vip_price = self.update_seat_configuration(#pass to method=update seat configuration edit will be happen inside that method
                                        "VIP",
                                        len(old_vip_rows),
                                        old_vip_seats,
                                        old_vip_price
                                    )
                        economy_rows, economy_seats, economy_price = self.update_seat_configuration(
                                    "ECONOMY",
                                    len(old_economy_rows),
                                    old_economy_seats,
                                    old_economy_price
                                )

                        update_show = showcontroller.update_show(show_id,screen_number,show_date,start_time,end_time)
                        update_seat = showcontroller.update_seats(show_id,vip_rows,#pass to controller - update seat method with given parameters
                                     vip_seats,
                                     vip_price,
                                     economy_rows,
                                     economy_seats,
                                     economy_price
                                )
                        if update_show is not None and update_seat is not None:
                                    print("Show and seats updated successfully")#if both true succes mesage print
                       
            else:
                          print("movie not found")
        
    def view_show(self,moviecontroller,showcontroller,theater_id):
         result = showcontroller.view_show(theater_id)
         if result:
                     print("\n========== AVAILABLE SHOWS ==========\n")
         
                     print("Show ID\t\tShow\t\tDate\t\tTime")
         
                     for show in result:
                         print(f"{show[0]}\t\t{show[1]}\t\t{show[2]}\t\t{show[3]}")
                     print("These are the available shows")
         else:
                       print("No shows available")
        
         
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
#first create an empty list
        old_vip_rows = []#to store a or b like..
        old_vip_seat_count = 0#initialize total num of vip seat =0
        old_vip_price = None#initialize price as none

        old_economy_rows = []#create empty list for economy row
        old_economy_seat_count = 0#total economy seat count =0
        old_economy_price = None#initialize prize =none
#loop through each seat record in result list
        for row in result:
#check wheather cureent is at vip
            if row[6] == "VIP":
                if row[7] not in old_vip_rows:## Add the row letter only if it has not already been added
                    old_vip_rows.append(row[7])# Example: Add "A" to ["A"]
# Increase the total VIP seat count by one
                old_vip_seat_count += 1# Example: 1 becomes 2
                old_vip_price = row[8]# Store the price of the current VIP seat Example: 500
# Otherwise, check whether the seat belongs to Economy
            elif row[6] == "Economy":
                # Add the row letter only if it is not already in the list
                if row[7] not in old_economy_rows:
                    old_economy_rows.append(row[7])# Example: Add "C"

                old_economy_seat_count += 1
                old_economy_price = row[8]
 # Calculate VIP seats per row using integer division
        old_vip_seats = old_vip_seat_count // len(old_vip_rows)#Example: 6 // 2 = 3
        old_economy_seats = old_economy_seat_count // len(old_economy_rows)
#Return the old seat configuration as a tuple
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

    def delete_show(self, moviecontroller,showcontroller,theater_id):

        result=self.view_show(moviecontroller,showcontroller,theater_id)#view show
        if not result:
            #print("No shows available to delete.")
            return
        while True:
            try:
                show_id = int(input("Enter Show ID: "))
                break
            except ValueError:
                print("Enter a valid Show ID.")

        result = self.search_show(showcontroller, show_id)#pass to controller to search

        if not result:
            print("Show not found.")
            return

        print("\nDo you want to delete this show?")
        print("1. Yes")
        print("2. No")
        while True:
            try:
                choice = int(input("Select an Option: "))

                if choice in [1, 2]:
                    break

                print("Please select 1 or 2.")#if person choosse other than 1 2

            except ValueError:
                print("Enter a valid option.")

        if choice == 1:

            result = showcontroller.delete_show(show_id)#pass to delete show in controller
            if result:
                print("Show deleted successfully")
            else:
                print("Deletion failed")

        elif choice == 2:
            print("Deletion cancelled")#nothing happned

    
    def customer_menu(self, customer_id,moviecontroller, theaterofficialcontroller, showcontroller,bookingcontroller):
        while True:
            print("""
================= CUSTOMER MENU =================

    1. View Your Tickets
    2. Book Tickets
    3. Exit Customer Menu

=================================================
            """)

            choice = input("SELECT AN OPTION: ")

            if choice == "1":
                self.view_your_tickets(bookingcontroller)

            elif choice == "2":
                self.book_tickets(customer_id,moviecontroller, theaterofficialcontroller,showcontroller,bookingcontroller)

            elif choice == "3":
                print("Exiting customer menu...")
                break

            else:
                print("Invalid option...")


    def book_tickets(self, customer_id,moviecontroller, theaterofficialcontroller,showcontroller,bookingcontroller):
        print(f"customer ID:{customer_id}")
        movies = self.view_movie(moviecontroller)#view movie

        if not movies:
            print("No movies available.")
            return

        while True:
            try:
                choice = int(input("Enter Movie ID: "))#id
            except ValueError:
                print("Enter a valid Movie ID.")
                continue

            valid = False

            for movie in movies:
                if movie[0] == choice:#this is for if there are movies with 1 and 2 but user enter 4 then return fail msg
                    valid = True
                    break

            if valid:
                theaters=theaterofficialcontroller.view_movie_based_theater(choice)#view theaters which have these movie
                if not theaters:
                     print("No theaters available")
                     return
                while True:
                    try:
                        your_theater = int(input("Enter the theater you want:"))#theater id
                    except ValueError:
                         print("Enter valid id....")
                         continue

                    valid = False
                    for theater in theaters:
                         if theater[0] == your_theater:
                              valid = True
                              break
                    if valid:
                         shows = showcontroller.view_show_based_theater(your_theater,choice)#show based theater with todays date
                         if not shows:
                              print("No shows available")
                              return
                         while True:
                              try:
                                   your_show = int(input("Enter the show you want:"))#show id
                              except ValueError:
                                   print("Enter valid id....")
                                   continue
                              valid=False
                              for show in shows:
                                   if show[0]==your_show:
                                        valid = True
                                        break
                              if valid:
                                 seats = showcontroller.view_seat_based_shows(your_show)#pass to seat
                                 while True:
                                    try:
                                            num_tickets = int(input("Enter the number of tickets:"))
                                    except ValueError:
                                            print("in number format")
                                            continue
                                    num_seats = showcontroller.check_number_of_seats(your_show,num_tickets)#pass to show controller-seatservice
                                    if not num_seats:
                                            return
                                      # Create an empty list to store the seat names selected by the customer     
                                    selected_seats = []# Example: ["A1", "A2"]
                                    # Create an empty list to store the database IDs of selected seats
                                    selected_seat_id = [] # Example: [101, 102]
# Repeat the seat selection process according to the number of tickets
                                    for i in range(num_tickets):
                                        # Keep asking until the customer enters a valid and available seat
                                        while True:# Ask the customer to enter a seat name
        # strip() removes extra spaces and upper() converts letters to uppercase
                                                    seat_name = input( f"Enter seat {i + 1} (e.g., A1): ").strip().upper()#upper or lower
# Check whether the customer has already selected this seat
  # Display an error message if the seat was selected previously
                                                    if seat_name in selected_seats:
                                                        print("Seat already selected!")
                                                        # Skip the remaining code and ask for another seat
                                                        continue
 # Initially assume that the entered seat is invalid
                                                    valid = False
 # Loop through all seats retrieved from the database
                                                    for seat in seats:
                                                            # Check whether the seat number matches AND its status is Available
                                                            if seat[2] == seat_name and seat[4] == "Available":
                                                                 # Mark the entered seat as valid
                                                                valid = True
                                                                # Store the database seat ID for booking_seat insertion
                                                                selected_seat_id.append(seat[0])
                                                                 # Stop searching because the matching seat was found
                                                                break

                                                    if not valid:
                                                            print("Invalid or unavailable seat!")
                                                            continue
# Store the valid seat name in the selected seats list
                                                    selected_seats.append(seat_name)
                                                    break

                                        print("Selected seats:", selected_seats)
                                        print("Selected seat ID:",selected_seat_id)
                                    updating_seats = showcontroller.update_booked_seats(your_show,selected_seats)
                                    if updating_seats:
                                         print("Seat booked succesfully..")
                                         display_details,total_amount = bookingcontroller.display_movie_details(choice,your_show,selected_seats)
                                         print(f"Movie:{display_details[0][0]}")
                                         print("Seats : ", end="")
                                         for seat in selected_seats:
                                            print(seat, end=" ")
                                            print()
                                         print(f"Total Amount:{total_amount}")
                                         booking_id = bookingcontroller.add_booking_details(customer_id,your_show,total_amount,num_tickets)
                                         booking_seat_id = bookingcontroller.add_booking_seat_details(booking_id,selected_seat_id)
                                         if booking_id and booking_seat_id:
                                              print("Booking details added succesfully.!")
                                         else:
                                              print("Booking details addition failed..!")
                                         return
                                    else:
                                         print("booking failed..")
                                 
                        
                              else:
                                print("Invalid Movie ID. Please enter a correct Movie ID.")

    def view_your_tickets(self,bookingcontroller):
          while True:
                     print("========== CUSTOMER ==========")
                     customer_mobile_num = input("Enter mobile number: ").strip()
         
                     if not customer_mobile_num.isdigit():
                         print("Please enter a valid mobile number.")
                         continue
                     
                     break
          result = bookingcontroller.view_your_tickets(customer_mobile_num)
          if result:
               print("These are the history of this customer...")
          else:
               print("No customer found!!")

    def view_transaction(self,reportingcontroller):
         result = reportingcontroller.view_all_transaction()