from sqlalchemy.orm import Session
from entities.Permision import Permision
from validate import schemas

class PermissionRepository():

    def get_permission_byId(db: Session, user_id: int):
        return db.query(Permision).filter(Permision.id == user_id).first()


    def get_permission(db: Session, name: str, skip: int = 0, limit: int = 100):
        return db.query(Permision).offset(skip).limit(limit).all()


    def create_permission(db: Session, permission: schemas.PermissionCreate):
        db_user = Permision(_id=permission.id, _name=permission.name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

