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
from controllers.showcontroller import ShowController
from dao.showdao import ShowDao

#movie managment
movie_dao = MovieDao()
movie_service=MovieService(movie_dao)
movie_controller=MovieController(movie_service)

#authetication admin
auth_dao = AuthDao()
auth_service = AuthenticationService(auth_dao)
auth_controller = AuthenticationController(auth_service)

#theater managment
theater_official_dao = TheaterOfficialDao()
theater_dao = TheaterDao()
theater_service = TheaterService(theater_dao)
theater_official_service= TheaterofficialService(theater_dao,theater_official_dao)
theater_official_controller = TheaterofficialController(theater_official_service,theater_service)

#show managment
show_dao = ShowDao()
show_service = ShowService(show_dao)
seat_dao = SeatService()
seat_service = SeatService(seat_dao)
show_controller = ShowController(show_service,seat_service)
viewer = Viewer()
#for displaying cli view common
viewer.starting_view(auth_controller,movie_controller,theater_official_controller,show_controller)