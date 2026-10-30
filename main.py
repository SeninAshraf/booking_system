from view.cliview import Viewer

from controllers.authcontroller import AuthenticationController
from services.authenticationservice import AuthenticationService
from dao.authenticationdao import AuthDao

from controllers.moviecontroller import MovieController
from services.movieservice import MovieService
from dao.moviedao import MovieDao

from services.theaterservice import TheaterService
from controllers.theaterofficialcontroller import TheaterofficialController
from services.theaterofficialservice import TheaterofficialService
from dao.theaterofficialdao import TheaterOfficialDao
from dao.theaterdao import TheaterDao

from services.showservice import ShowService
from services.seatservice import SeatService
from dao.seatdao import SeatDAO
from controllers.showcontroller import ShowController
from dao.showdao import ShowDao

from controllers.bookingcontroller import BookingController
from services.bookingservice import BookingService
from dao.bookingdao import BookingDAO

from controllers.reportingcontroller import ReportingController
from services.reportingservice import ReportingService

#movie managment
movie_dao = MovieDao()#creating objects to use classses like movie_dao.get_movies()
movie_service=MovieService(movie_dao)
movie_controller=MovieController(movie_service)



#theater managment
theater_official_dao = TheaterOfficialDao()
theater_dao = TheaterDao()
theater_service = TheaterService(theater_dao)
theater_official_service= TheaterofficialService(theater_dao,theater_official_dao)
theater_official_controller = TheaterofficialController(theater_official_service,theater_service)

#show managment
show_dao = ShowDao()
show_service = ShowService(show_dao,movie_dao)
seat_dao = SeatDAO()
seat_service = SeatService(seat_dao)
show_controller = ShowController(show_service,seat_service)

#customer managment
booking_dao =BookingDAO()
booking_service = BookingService(booking_dao)
booking_controller=BookingController(show_service,seat_service,booking_service)

#reporting managment
reporting_service = ReportingService(booking_dao)
reporting__controller=ReportingController(reporting_service)
#authetication admin
auth_dao = AuthDao()
auth_service = AuthenticationService(auth_dao)
auth_controller = AuthenticationController(auth_service)




viewer = Viewer()


#for displaying cli view common
viewer.starting_view(auth_controller,movie_controller,theater_official_controller,show_controller,booking_controller,reporting__controller)#passing controller methods so viewer object can use it