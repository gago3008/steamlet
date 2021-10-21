from sqlalchemy.sql.sqltypes import TIMESTAMP
from . import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class CustomerOrder(Base):
    __tablename__ = "CustomerOrder"

    _id = Column(Integer, primary_key=True, auto_increment=True)
    _userId = Column(String(50), unique=False)
    _totalPrice = Column(Integer, unique=False)
    _createTime = Column(TIMESTAMP, unique=False)
    _endTime = Column(TIMESTAMP, unique=False)

 