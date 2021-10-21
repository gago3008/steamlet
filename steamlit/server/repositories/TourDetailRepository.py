from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import DATETIME, TIME, Date, DateTime
from entities.TourDetail import TourDetail
from validate import schema
from common.convertDB import to_dict

class TourDetailRepository():

    def get_TourDetail_byTourId(self, db: Session, tourid: int):
        return db.query(TourDetail).filter(TourDetail._tourId == tourid).all()
  
    def filter_Tour(self, db: Session, totalpeople : int,quantiny: int, start_time: DateTime = datetime.now() , end_time: DateTime = datetime.now(),skip : int = 0, limit: int = 100):
        return db.query(TourDetail).filter(TourDetail._quantiny == quantiny, TourDetail._startTime == start_time, TourDetail._endTime == end_time, TourDetail._totalPeople == totalpeople).offset(skip).limit(limit).all()

    def get_Tour_byId(self, db: Session, tourId: int):
        return db.query(TourDetail).filter(TourDetail._id == tourId).first()

    def create_TourDetail(self, db: Session, tourdetail: schema.TourDetailCreate):
        try:
            db_Tour = TourDetail(
                _quantiny = tourdetail.quantiny,
                _totalPeople = tourdetail.totalPeople,
                _starttime = tourdetail.startTime,
                _categoryId = tourdetail.categoryId,
                _endtime = tourdetail.endTime,
                _RemoveTime = tourdetail.removetime,
                _price =  tourdetail.price
                )
            db.add(db_Tour)
            db.commit()
            db.refresh(db_Tour)
            return True
        except:
            print("Error !")
            return False

    def update_TourDetail(self, db: Session, tourdetail : schema.TourUpdate):
        try:
            db_TourDetail = TourDetail(
                _totalPeople = tourdetail.totalPeople,
                _starttime = tourdetail.startTime,
                _categoryId = tourdetail.categoryId,
                _endtime = tourdetail.endTime,
                _RemoveTime = tourdetail.removetime
                )
            db.delete(db_TourDetail)
            db.commit()
            db.refresh()
            return True
        except:
            return False

    def delete_tour(self, db: Session, tourId):
        try:
            db_TourDetail = self.get_Tour_byId(tourId= tourId)
            db.delete(db_TourDetail)
            db.commit()
            db.refresh()
            return True
        except:
            return False
