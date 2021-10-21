from sqlalchemy.orm import Session
from entities.CusomterOrder import CustomerOrder
from validate import schema


class CustomerOrderRepository():

    def get_CustomerOrder_byId(self, db: Session, _id: int):
        return db.query(CustomerOrder).filter(CustomerOrder._id == _id).first()


    def get_CustomerOrder_byName(self, db: Session, name: str):
        return db.query(CustomerOrder).filter(CustomerOrder._userId == action).first()


    def get_actions(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Actions).offset(skip).limit(limit).all()


    def create_action(self, db: Session, action: schema.ActionCreate):
        _name = action._name 
        db_action = Actions(_name = _name)
        db.add(db_action)
        db.commit()
        db.refresh(db_action)
        return db_action


    def delete_actions(self, db: Session, action: Actions):
        db_action = action
        db.delete(db_action)
        db.commit()
        db.refresh(db_action)
        return db_action

