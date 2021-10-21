from typing import Tuple
from entities import Users
from repositories import UserRepository
from middlewares.securities import Security
from validate import schema
from config.configs import config_model
from api import UserSession, SessionMap
from repositories import PermisionRepository
from common.convertDB import to_dict

class PermissionService():

    permissionRepo = PermisionRepository()

    def getPermissionById(self, permissionId):
        listPermission = self.permissionRepo.get_Permission_byId(permissionId)
        return listPermission
    
    def getPermissionName(self, permission):
        permission = to_dict(permission)
        return permission['_name']

            