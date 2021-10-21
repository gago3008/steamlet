from entities import Users
from repositories import UserRepository
from middlewares.securities import Security
from validate import schema
from config.configs import config_model
from api import UserSession, SessionMap
from repositories import UserPermissionRepository
from repositories import PermisionRepository
from services import PermissionService, UserPermissionService

class UserService():
    security = Security(config_model)

    userPermissionService = UserPermissionRepository()

    permissionService = PermissionService()


    def getRolePermission(self, userId):
        listPermissionId = self.userPermissionService.get_listPermissionId_byUserId(userId)
        get_Permission = lambda x : self.permissionService.getPermissionById(x)
        listPermission = [ get_Permission(PermissionId) for PermissionId in listPermissionId ]
        listPermissionName = [ self.permissionService.getPermissionName(Permission) for Permission in listPermission ]
        
        return listPermissionName


    def check_login(self, user: schema.UserLogin):
        userExist = self.userRepository.get_user_by_username(userame=user.usename)

        if userExist:
            sessionId = self.security.create_security(user.dict())
            x_access_token = self.security.create_x_access_token(user.dict())
            SessionMap[x_access_token] = sessionId
            list_role = self.getRolePermission()
            UserSession[sessionId] = {"user" : user, "role" : list_role, "action" : list_action}
