from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import DateTime
from entities.CustomerOrder import CustomerOrder
from validate import schema
import datetime


class CustomerOrderRepository():

    def get_CustomerOrder_byId(self, db: Session, _id: int):
        return db.query(CustomerOrder).filter(CustomerOrder._id == _id).first()

    def get_CustomerOrder_byUserId(self, db: Session, userId = int, price= int, createTime:DateTime = datetime.now(), endTime : DateTime=None):
        return db.query(CustomerOrder).filter(CustomerOrder._userId==userId, CustomerOrder._totalPrice==price, CustomerOrder._createTime==createTime, CustomerOrder._endTime==endTime).first()

    def create_customerorder(self, db: Session, customerOrder: schema.CustomerOrderCreate):
        try:
            db_customerOrder = CustomerOrder( _userId = customerOrder._userId, _totalPrice = customerOrder._totalPrice, _createTime= customerOrder._createTime, _endTime = customerOrder._endTime )
            db.add(db_customerOrder)
            db.commit()
            db.refresh(db_customerOrder)
            return True
        except:
            return False

    def update_customerOrder(self, db: Session, customerOrder: schema.CustomerOrderUpdate):
        try:
            db_customerOrder = CustomerOrder( _userId = customerOrder._userId, _totalPrice = customerOrder._totalPrice, _createTime= customerOrder._createTime, _endTime = customerOrder._endTime )
            db.add(db_customerOrder)
            db.commit()
            db.refresh(db_customerOrder)
            return True
        except:
            return False

    def delete_customerorder(self, db: Session, customerOrderId: int):
        try:
            db_customerOrder = self.get_CustomerOrder_byId(customerOrderId)
            db.add(db_customerOrder)
            db.commit()
            db.refresh()
            return True
        except:
            return False

