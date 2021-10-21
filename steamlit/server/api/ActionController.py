from os import stat
from flask.json import jsonify
from pydantic.networks import HttpUrl
from sqlalchemy.sql.sqltypes import Integer
from starlette.requests import HTTPConnection
from api import UserSession, SessionMap
from fastapi import APIRouter, File, UploadFile ,Depends , Request
from sqlalchemy.orm import Session
from common.convertDB import to_list
from fastapi import HTTPException
from repositories.UserRepository import UserRepository
from validate import schema
from api import get_db
from middlewares.authenicate import authenicate_required
from middlewares.securities import Security
from config.configs import config_model


security = Security(config_model)

router = APIRouter()

@router.get("/users/")
@authenicate_required
def get_user(db: Session = Depends(get_db)):
    db_user = to_list(UserRepository.get_users(db))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")


@router.post("/get-permission/")
@authenicate_required
def create_user(user: schema.UserCreate ,db: Session = Depends(get_db)):
    db_user = to_list(UserRepository.get_users(db))
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered!")
    return UserRepository.create_user(db=db, user=user)

@router.get('/get-user')
@authenicate_required
def create_user(user: schema.listUser ,db: Session = Depends(get_db)):
    db_user = to_list(UserRepository.get_users(db))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserRepository.create_user(db=db, user=user)


@router.delete('delete-user')
@authenicate_required
def delete_user(user: schema.deleteUser ,db : Session = Depends(get_db)):
    db_user =  to_list(UserRepository.get_user_by_username(db, user.username))
    if len(db_user) == 0:
        raise HTTPException(status_code=400, detail="User not exist!")
    return UserRepository.delete_user(db=db, user=user)

