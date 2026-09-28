from view.cliview import Viewer

from controllers.authcontroller import AuthenticationController
from services.authenticationservice import AuthenticationService
from dao.authenticationdao import AuthDao



#authetication admin
auth_dao = AuthDao()
auth_service = AuthenticationService(auth_dao)
auth_controller = AuthenticationController(auth_service)

#auth theater official
#theater_dao = TheaterOfficialDao()
#auth_service = Th(auth_dao)
#theater_controller = TheaterController(theater_service)

viewer = Viewer()
#for displaying cli view common
viewer.starting_view(auth_controller)