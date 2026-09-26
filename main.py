from view.cliview import Viewer
from controllers.authcontroller import AuthenticationController
from services.authenticationservice import AuthenticationService
from dao.authenticationdao import AuthDao


auth_dao = AuthDao()

auth_service = AuthenticationService(auth_dao)

auth_controller = AuthenticationController(auth_service)

viewer = Viewer()

viewer.login(auth_controller)