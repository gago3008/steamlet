from entities import Users
from repositories import UserRepository
from middlewares.securities import Security
from validate import schema
from config.configs import config_model
from api import UserSession, SessionMap
from repositories import UserPermissionRepository
from services import PermissionService
from entities.UserPermission import UserPermision
from log import SysLog
from typing import List

class UserPermissionService():
    security = Security(config_model)

    userPermissionRepo = UserPermissionRepository()

    permissionService = PermissionService()

    def get_UserPermission(self, userId : str):
        userPermission = self.userPermissionRepo.get_UserPermission(userId)
        userPermission = UserPermision.transformObject(userPermission)
        return userPermission


    def get_listPermissionId_byUserId(self, userId : str) -> List[str]:
        listPermissionId = [ userPermission._permissionId for userPermission in self.get_UserPermission(userId)]
        return listPermissionId