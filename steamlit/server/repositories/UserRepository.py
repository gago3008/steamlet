from sqlalchemy.orm import Session
from entities.Users import Users
from validate import schema
from common.convertDB import to_list, to_dict

class UserRepository():
    __tablename__ = "users"

    def get_user_byId(db: Session, user_id: int):
        return db.query(Users).filter(Users.id == user_id).first()


    def get_user_by_username(db: Session, usename: str):
        return to_dict(db.query(Users).filter(Users._username == usename).first())

    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Users).offset(skip).limit(limit).all()


    def create_user(db: Session, user: schema.UserCreate):
        fake_hashed_password = user.password + "_notreallyhashed"
        db_user = Users(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def delete_user(db: Session, user: Users):
        try:
            db_user = user
            db.delete(db_user)
            db.commit()
            db.refresh()
            return True
        except:
            return False
